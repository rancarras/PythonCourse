%------------------------------Deepak Tomar-------------------------------
% programm for import, x window range, cosmic ray removal, smooth, baseline
% of combined spectra exported before  and export final plot in a Single spectra
close all;
clear all;
clc;


%load files
[filename, path] = uigetfile('*.asc','MultiSelect','on');
cd(path);
files = string(filename);
f1=erase(filename,".asc");
[token,f2]=strtok(f1, ' ');
Srate =string(f1);

%window
figure('Name','Data manupulation window');


%Select Parameters
prompt1 = {'Enter Raman Shift range in cm^{-1} (xmin xmax):'};
dlgtitle1 = 'Select Spectral Range';
dims1 = [1 35];
definput1 = {'0 4000'};
answer1 = inputdlg(prompt1,dlgtitle1,dims1,definput1);
rin = split(answer1);
xmin = str2num(rin{1});
xmax = str2num(rin{2});


% Remove cosmic ray or spikes
quest2 = 'Do you want to remove Cosmic Ray or Spikes?';
opts.Interpreter = 'tex';
opts.Default = 'No';
answer2 = questdlg(quest2,'Cosmic Ray Removal','Yes','No',opts);
switch answer2
    case 'Yes'
            prompt2 = {'Threshold value:','Enter value for the mean of its immediate neighbors (within a 2m+1 values window):'};
            dlgtitle2 = 'Cosmic Ray or Spikes Removal Test Run';
            dims2 = [1 70];
            definput2 = {'3.5','3'};
            answer21 = inputdlg(prompt2,dlgtitle2,dims2,definput2);
            thrld = str2double(answer21{1});
            m = str2double(answer21{2});
    case 'No'
        disp(['Canceled Cosmic Ray or Spikes Removal Test Run'])
end

% Smooth data
quest3 = 'Do you want to smooth data by Savitzky-Golay filter?';
opts.Interpreter = 'tex';
opts.Default = 'No';
answer3 = questdlg(quest3,'Smooth Data Parameters','Yes','No',opts);
switch answer3
    case 'Yes'
        prompt3 = {'Enter span value (Number of data points for calculating the smoothed value):','Enter polynomial degree value (must be less than span):'};
        dlgtitle3 = 'Smooth data Input';
        dims3 = [1 60];
        definput3 = {'5','2'};
        answer31 = inputdlg(prompt3,dlgtitle3,dims3,definput3);
         pt_val = str2double(answer31{1});
         odr = str2double(answer31{2});
    case 'No'
        disp(['continue without smoothdata'])
end
hold on;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
% Rubberband baseline correction
quest4 = 'Do you want to perform baseline correction?';
opts.Interpreter = 'tex';
opts.Default = 'No';
answer4 = questdlg(quest4,'Baseline Correction','Yes','No',opts);
switch answer4
    case 'Yes'
            prompt4 = {'Enter the number of iterations:','Enter polynomial degree (must be >1):'};
            dlgtitle4 = 'Rubberband Baseline Correction';
            dims4 = [1 70];
            definput4 = {'1','2'};
            answer41 = inputdlg(prompt4,dlgtitle4,dims4,definput4);
            iterns = str2double(answer41{1});
            polyorder= str2double(answer41{2});
    case 'No'
        disp(['Canceled Cosmic Ray or Spikes Removal Test Run.'])
end


for j=1:length(files)
D=load(files(j));
x1= D(:,1);
y1 =D(:,2);

% Plot data
[x,y]  =selectrange(x1,y1,xmin,xmax);
subplot(2,2,1)
ramanplot(x,y,files,j);
title('Raw Data')
hold on;


% Remove cosmic ray or spikes
switch answer2
    case 'Yes'
            I_out2=cosmic_ray_z_score(y,m,thrld);
            y=I_out2;
            subplot(2,2,2)
            ramanplot(x,y,files,j);
            title('After Cosmic Ray Removal ');
end
hold on;

% Smooth data
switch answer3
    case 'Yes'
         ysmooth = smooth(y,pt_val,'sgolay',odr);
         y=ysmooth;
        subplot(2,2,3)
        ramanplot(x,y,files,j);
        title('Smooth Data');
end
hold on;

% Rubberband baseline correction
switch answer4
    case 'Yes'
            I_out4=rubberband_baseline(x,y,iterns,polyorder);
            y=I_out4;
            subplot(2,2,4)
            ramanplot(x,y,files,j);
            title('Baseline corrected data')
end   

yFinal(:,j+1)=y;
hold on;
end
yFinal(:,1)=x;

figure('Name','Final Data Window');
for j=1:length(files)
ramanplot(x,yFinal(:,j+1),Srate,j);
hold on
end

title('20150120 APFN',Srate(1),'fontweight','bold','fontsize',18);
files1= ['wavenumber' files];
exprt=[files1;yFinal];
writematrix(exprt,'combined.txt','Delimiter','tab')
% width=18; %width of figure in cm
% height=10; %height of figure in cm
% set(gca,'units','centimeters','outerposition',[9 2 width height])
plotedit on;
% plotedit off;






%Functions are defined here


%select spectral window
function [x,y]  =selectrange(x,y,xmin,xmax)
y(x<xmin|x>xmax)=[];
x(x<xmin|x>xmax)=[];
end


%Plot spectrum
function plotf = ramanplot(x,y,files,j)
plotf=plot(x,y,'-','LineWidth',3,'DisplayName',files(j));
xlabel('\bf{Raman Shift (cm^{-1})}','fontweight','bold','fontsize',18);
ylabel('\bf{Intensity (Counts)}','fontweight','bold','fontsize',18);
set(gca,'fontweight','bold','fontsize',18,'LineWidth', 3)
lgd=legend('show','FontSize',18,'TextColor','black','Location','best');
axis('tight')
set(gcf, 'units','normalized','outerposition',[0 0 1 1]);
end


% Remove cosmic ray or spikes
function y_out=cosmic_ray_z_score(y,m,threshold)
% Whitaker and Hayes’ modified Z-score based approach for spike detection
delta_int = diff(y);
 delta_median_int = median(delta_int);
 delta_mad_int = median(abs(delta_int - delta_median_int));%median absolute deviation (MAD) 
 intensity_modified_z_score = abs(0.6745 * (delta_int - delta_median_int) / delta_mad_int);
 spikes = (intensity_modified_z_score) > threshold;%1 is assigned to spikes, 0 to non-spikes:
%Fixing the Raman spectrum
 y_out = y;
 for n1=1:length(spikes)
   if spikes(n1) ~= 0 %If we have an spike in position n1
   w = (n1-1-m):(n1+m); % we select 2 m + 1 points around our spike
   w1=w(w>0);
   w2 = w1(spikes(w1) == 0); % From such interval, we choose the ones which are not spikes
   y_out(n1) = mean(y(w2)); % and we average their values
   end
 end
end


% Rubberband baseline correction
function yout4=rubberband_baseline(x,y,iteration,n)
for j=1:iteration
F= (max(y)-min(y))/10;
x0=(x(1)+x(end))*0.5;
fx1=(abs(x-x0).^n);
fx2=(abs(x(end)-x0).^n);
fx=F*(fx1./fx2);
%Rubberband correction
yAdd=y+fx;
P=[x yAdd];
[k,~] = convhull(P);
c11=P(k,1);
c22=P(k,2);
L = find((c11) == max(x));
c1=c11([1:L]);
c2=c22([1:L]);
c=interp1(c1,c2,x,'linear');
y=yAdd-c;
end
yout4=y;
end


