clear all
clc
tic
info=fitsread('selkone.fits','Binarytable');
allid=info{:,2};
allhjd=info{:,4}-2450000;
allmag=info{:,6};
allflag=info{:,8};
alltype=info{:,9};
[cntr_01,oid,ra,dec,field,ccdid,qid,filtercode,ngoodobs,ngoodobsrel,nobs,nobsrel,refmag,refmagerr]=textread('selkonefulltable.txt','%f%s%f%f%f %f%f %s%f %f%f%f %f%f');
%
qqq=max(cntr_01);
%
b0y=zeros(1,qqq);b1y=zeros(1,qqq);b2y=zeros(1,qqq);b3y=zeros(1,qqq);b4y=zeros(1,qqq);
amp1y=zeros(1,qqq);c3y=zeros(1,qqq);
c4y=zeros(1,qqq);dmy=zeros(1,qqq);
per=zeros(1,qqq);psd=zeros(1,qqq);
%
a0y2=zeros(1,qqq);a1y2=zeros(1,qqq);a2y2=zeros(1,qqq);a3y2=zeros(1,qqq);a4y2=zeros(1,qqq);
b0y2=zeros(1,qqq);b1y2=zeros(1,qqq);b2y2=zeros(1,qqq);b3y2=zeros(1,qqq);b4y2=zeros(1,qqq);
amp2y=zeros(1,qqq);c3y2=zeros(1,qqq);
c4y2=zeros(1,qqq);dmy2=zeros(1,qqq);
per2=zeros(1,qqq);psd2=zeros(1,qqq);
%
psd22=zeros(1,qqq);
ccc=0.0:0.01:2.0;
ccc3=ccc';
%
rax=zeros(1,qqq);decx=zeros(1,qqq);
p2s=zeros(1,qqq);nn=zeros(1,qqq);

for i=1:max(cntr_01) 
    x=find(abs(cntr_01-i)<0.1&strcmp(filtercode,'zg')>0);
    magin=[];
    hjdin=[];
    if ~isempty(x)
    rax(i)=ra(x(1));
    decx(i)=dec(x(1));  
    for k=1:length(x)
    oid1=oid(x(k));
    nnn1=find(abs(allid-str2double(oid1))<0.01&strcmp(alltype,'zg')>0&allflag<30000);
    magin=[magin;allmag(nnn1)];
    hjdin=[hjdin;allhjd(nnn1)];
    end
    end
mu=median(magin);
out=abs(magin-mu)>2;
magin(out)=[]; 
hjdin(out)=[];
mu1=median(magin);
std1=std(magin);
out1=abs(magin-mu1)>3*std1;
magin(out1)=[]; 
hjdin(out1)=[];
[hjd,kkk]=sort(hjdin);
mag=magin(kkk);
aa=unique(hjd);
[ta,tb]=ismember(aa,hjd);
khjd2=hjd(tb); 
kmag2=mag(tb);
xxx=khjd2(2:length(khjd2))-khjd2(1:length(khjd2)-1);
selxxx=find(xxx<0.001);
khjd2(selxxx)=[];
kmag2(selxxx)=[];
if length(kmag2)>30
magconstant=kmag2.*0.0+15.243;
Pfa = [0.01 0.001 0.0001 0.00001 0.000001 0.0000001 0.00000001];
% last_fap=ones(10,1);
% last_fap(:,end)=0.1;
% Pfa=cumprod(last_fap);
Pd = 1 - Pfa;
[pxx,f,pth]=plomb(kmag2,khjd2,40,100,'normalized','Pd',Pd);
[pk1x,indexx]=max(pxx);
fap_matrix=[pth,Pfa'];  
fit_fap=fit(fap_matrix(:,1),log10(fap_matrix(:,2)),'poly1');
one_hha=max(pxx);
fap_one= feval(fit_fap,one_hha); 
[pxxsel,fsel]=plomb(magconstant,khjd2,1,'normalized');
[pksel,f0sel] = findpeaks(pxxsel,fsel,'minpeakheight',10);
pxxsel1=0.0.*pxxsel+1.0;
for isel=1:length(pksel)
    kisel=find(abs(fsel-f0sel(isel))<0.00001);
    pxx(kisel-1:kisel+1,1)=0.001;
end
halfmaxpxx=max(pxx)*0.5;
[pk,f0] = findpeaks(pxx,f,'minpeakheight',halfmaxpxx);
if max(pk)>0
[pk1,index]=max(pk);
flast=f0(index);
period=1.0/flast;
per(i)=period;
psd(i)=max(pxx);
fap1(i)=fap_one;
d=khjd2./period-fix(khjd2./period);
d1=d+1.0;
d2=[d;d1]; 
kmag3=[kmag2;kmag2];
f2=fittype('a0+a1*cos(2*pi*x)+b1*sin(2*pi*x)+a2*cos(4*pi*x)+b2*sin(4*pi*x)+a3*cos(6*pi*x)+b3*sin(6*pi*x)+a4*cos(8*pi*x)+b4*sin(8*pi*x)+a5*cos(10*pi*x)+b5*sin(10*pi*x)+a6*cos(12*pi*x)+b6*sin(12*pi*x)');

[f1,gof]=fit(d2,kmag3,f2,'StartPoint', [1, 0.001,  0.001,  0.001,  0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]);
coeffs=coeffvalues(f1);
dmy(i)=mean(kmag2);
amp1y(i)=max(f1(d))-min(f1(d));
c3y(i)=gof.adjrsquare;
c4y(i)=gof.rmse;
canmag=kmag2-f1(d);
[pxx2,fx2]=plomb(canmag,khjd2,40,100,'normalized');
[pxx2,fx2,pth2]=plomb(canmag,khjd2,40,100,'normalized','Pd',Pd);
fap_two_matrix=[pth2,Pfa'];
fit_two_fap=fit(fap_two_matrix(:,1),log10(fap_two_matrix(:,2)),'poly1');
halfmaxpxx2=max(pxx2)*0.5;
[pmax2,tto]=max(pxx2);
two_hh=max(pxx2);
fap_two= feval(fit_two_fap,two_hh); 
psd22(i)=pmax2;
p2s(i)=1/fx2(tto);
fap2(i)=fap_two;
[pk2,f02]=findpeaks(pxx2,fx2,'minpeakheight',halfmaxpxx2);
if max(pk2)>0
[pk12,index2]=max(pk2);
flast2=f02(index2);
period2=1.0/flast2;
if abs(period2/period-0.77)>0.03 && abs(period/period2-0.77)>0.03
    y=find(abs(1./f02./period-0.77)<0.03|abs(f02.*period-0.77)<0.03);
    ooy=f02(y);
    oox=pk2(y);
    [cc,dd]=sort(oox);
    if ~isempty(y)
       period2=1/ooy(end);
       pmax2=oox(end);
    end
end     
per2(i)=period2;
period_ratio(i)=period2./period;
psd2(i)=pmax2;
dx=khjd2./period2-fix(khjd2./period2);
dx1=dx+1.0;
dx2=[dx;dx1];
canmag3=[canmag;canmag];
[f2xx,gof2]=fit(dx2,canmag3,f2,'StartPoint', [1, 0.001,  0.001,  0.001,  0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]);
coeffs2=coeffvalues(f2xx);
dmy2(i)=mean(canmag);
amplitude=max(f2xx(dx))-min(f2xx(dx));
amp2y(i)=amplitude;
c3y2(i)=gof2.adjrsquare;
c4y2(i)=gof2.rmse;




if fap_two>-3

figure(1)
subplot('position',[0.08,0.57,0.40,0.40])
plot(d2,kmag3,'r.','markersize',10);
hold on
plot(ccc3,f1(ccc3),'g','LineWidth',4);
xlim([-0.1 2.1])
ylim('auto')
set(gca,'YDir','reverse');
xlabel('pulsation phase','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('r (mag)','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.08,0.08,0.40,0.40])
plot(f,pxx,'-','LineWidth',2.5)
hold on
plot(f0(index),pk1,'o','MarkerFaceColor',[0.4940 0.1840 0.5560],'MarkerEdgeColor',[0.6350 0.0780 0.1840],'markersize',7)
xlabel('Frequency','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('PSD','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','off')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.57,0.57,0.40,0.40])
plot(dx2,canmag3,'r.','markersize',10);
hold on
plot(ccc3,f2xx(ccc3),'g','LineWidth',4);
xlim([-0.1 2.1])
ylim('auto')
set(gca,'YDir','reverse');
xlabel('pulsation phase','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('\Delta r (mag) ','Interpreter','tex','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.57,0.08,0.40,0.40])
plot(fx2,pxx2,'-','LineWidth',2.5)
hold on
plot(f02(index2),pk12,'o','MarkerFaceColor',[0.4940 0.1840 0.5560],'MarkerEdgeColor',[0.6350 0.0780 0.1840],'markersize',7)
xlabel('Frequency','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('PSD','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off
set(gcf,'OuterPosition',[1,1,950,580], 'position',[1,1,950,580]);
savepath='/Users/qijia/Downloads/jq/6.5/newpsd/fapover3';
fileName = ['ra=' num2str(rax(i)) 'dec=' num2str(decx(i)) '.jpg'];
fullPath = fullfile(savepath, fileName);
saveas(figure(1), fullPath);
close all
end

if fap_two<-3 & amplitude<0.01;
figure(3)
subplot('position',[0.08,0.57,0.40,0.40])
plot(d2,kmag3,'r.','markersize',10);
hold on
plot(ccc3,f1(ccc3),'g','LineWidth',4);
xlim([-0.1 2.1])
ylim('auto')
set(gca,'YDir','reverse');
xlabel('pulsation phase','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('r (mag)','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.08,0.08,0.40,0.40])
plot(f,pxx,'-','LineWidth',2.5)
hold on
plot(f0(index),pk1,'o','MarkerFaceColor',[0.4940 0.1840 0.5560],'MarkerEdgeColor',[0.6350 0.0780 0.1840],'markersize',7)
xlabel('Frequency','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('PSD','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','off')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.57,0.57,0.40,0.40])
plot(dx2,canmag3,'r.','markersize',10);
hold on
plot(ccc3,f2xx(ccc3),'g','LineWidth',4);
xlim([-0.1 2.1])
ylim('auto')
set(gca,'YDir','reverse');
xlabel('pulsation phase','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('\Delta r (mag) ','Interpreter','tex','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.57,0.08,0.40,0.40])
plot(fx2,pxx2,'-','LineWidth',2.5)
hold on
plot(f02(index2),pk12,'o','MarkerFaceColor',[0.4940 0.1840 0.5560],'MarkerEdgeColor',[0.6350 0.0780 0.1840],'markersize',7)
xlabel('Frequency','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('PSD','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off
set(gcf,'OuterPosition',[1,1,950,580], 'position',[1,1,950,580]);
savepath2='/Users/qijia/Downloads/jq/6.5/newpsd/faploweramplower';
fileName2 = ['ra=' num2str(rax(i)) 'dec=' num2str(decx(i)) '.jpg'];
fullPath2 = fullfile(savepath2, fileName2);
saveas(figure(3), fullPath2);
close all
end

end
end
end
nn(i)=i;
end

selkone_fap=[rax',decx',per',psd',amp1y',dmy',fap1',per2',psd2',amp2y',dmy2',fap2',psd22',p2s',period_ratio'];
save selkone_fap

datacolumns = {'ra','dec','per','psd','amp1y','mag','fap1','per2','psd2','amp2y','mag2','fap2','psd22','p2s','ratio'};
newtable=table(selkone_fap(:,1),selkone_fap(:,2),selkone_fap(:,3),selkone_fap(:,4),selkone_fap(:,5),selkone_fap(:,6),selkone_fap(:,7),selkone_fap(:,8),selkone_fap(:,9),selkone_fap(:,10),selkone_fap(:,11),selkone_fap(:,12),selkone_fap(:,13),selkone_fap(:,14),selkone_fap(:,15),'VariableNames',datacolumns);
writetable(newtable, 'ansselkonefap.csv');

% trasix=selkone_fap;
% fapfind=find(fap_two>-3);
% dsda=trasix(fapfind,:);
% datacolumns = {'ra','dec','per','psd','amp1y','mag','fap1','per2','psd2','amp2y','mag2','fap2','psd22','p2s','ratio'};
% newtable=table(dsda(:,1),dsda(:,2),dsda(:,3),dsda(:,4),dsda(:,5),dsda(:,6),dsda(:,7),dsda(:,8),dsda(:,9),dsda(:,10),dsda(:,11),dsda(:,12),dsda(:,13),dsda(:,14),dsda(:,15),'VariableNames',datacolumns);
% writetable(newtable, 'fapcondition.csv');
% 
% rasda=selkone_fap;
% fsdfs=find(fap<-3&amp2y<0.01);
% sdawd=rasda(fsdfs,:);
% datacolumns = {'ra','dec','per','psd','amp1y','mag','fap1','per2','psd2','amp2y','mag2','fap2','psd22','p2s','ratio'};
% newtable=table(sdawd(:,1),sdawd(:,2),sdawd(:,3),sdawd(:,4),sdawd(:,5),sdawd(:,6),sdawd(:,7),sdawd(:,8),sdawd(:,9),sdawd(:,10),sdawd(:,11),sdawd(:,12),sdawd(:,13),sdawd(:,14),sdawd(:,15),'VariableNames',datacolumns);
% writetable(newtable, 'fapandampcondition.csv');
% 

clear all
clc

info=fitsread('selkfour.fits','Binarytable');
allid=info{:,2};
allhjd=info{:,4}-2450000;
allmag=info{:,6};
allflag=info{:,8};
alltype=info{:,9};
[cntr_01,oid,ra,dec,field,ccdid,qid,filtercode,ngoodobs,ngoodobsrel,nobs,nobsrel,refmag,refmagerr]=textread('selkfourfulltable.txt','%f%s%f%f%f %f%f %s%f %f%f%f %f%f');
%
qqq=max(cntr_01);
%
b0y=zeros(1,qqq);b1y=zeros(1,qqq);b2y=zeros(1,qqq);b3y=zeros(1,qqq);b4y=zeros(1,qqq);
amp1y=zeros(1,qqq);c3y=zeros(1,qqq);
c4y=zeros(1,qqq);dmy=zeros(1,qqq);
per=zeros(1,qqq);psd=zeros(1,qqq);
%
a0y2=zeros(1,qqq);a1y2=zeros(1,qqq);a2y2=zeros(1,qqq);a3y2=zeros(1,qqq);a4y2=zeros(1,qqq);
b0y2=zeros(1,qqq);b1y2=zeros(1,qqq);b2y2=zeros(1,qqq);b3y2=zeros(1,qqq);b4y2=zeros(1,qqq);
amp2y=zeros(1,qqq);c3y2=zeros(1,qqq);
c4y2=zeros(1,qqq);dmy2=zeros(1,qqq);
per2=zeros(1,qqq);psd2=zeros(1,qqq);
%
psd22=zeros(1,qqq);
ccc=0.0:0.01:2.0;
ccc3=ccc';
%
rax=zeros(1,qqq);decx=zeros(1,qqq);
p2s=zeros(1,qqq);nn=zeros(1,qqq);

for i=1:max(cntr_01) 
    x=find(abs(cntr_01-i)<0.1&strcmp(filtercode,'zg')>0);
    magin=[];
    hjdin=[];
    if ~isempty(x)
    rax(i)=ra(x(1));
    decx(i)=dec(x(1));  
    for k=1:length(x)
    oid1=oid(x(k));
    nnn1=find(abs(allid-str2double(oid1))<0.01&strcmp(alltype,'zg')>0&allflag<30000);
    magin=[magin;allmag(nnn1)];
    hjdin=[hjdin;allhjd(nnn1)];
    end
    end
mu=median(magin);
out=abs(magin-mu)>2;
magin(out)=[]; 
hjdin(out)=[];
mu1=median(magin);
std1=std(magin);
out1=abs(magin-mu1)>3*std1;
magin(out1)=[]; 
hjdin(out1)=[];
[hjd,kkk]=sort(hjdin);
mag=magin(kkk);
aa=unique(hjd);
[ta,tb]=ismember(aa,hjd);
khjd2=hjd(tb); 
kmag2=mag(tb);
xxx=khjd2(2:length(khjd2))-khjd2(1:length(khjd2)-1);
selxxx=find(xxx<0.001);
khjd2(selxxx)=[];
kmag2(selxxx)=[];
if length(kmag2)>30
magconstant=kmag2.*0.0+15.243;
Pfa = [0.01 0.001 0.0001 0.00001 0.000001 0.0000001 0.00000001];
% last_fap=ones(10,1);
% last_fap(:,end)=0.1;
% Pfa=cumprod(last_fap);
Pd = 1 - Pfa;
[pxx,f,pth]=plomb(kmag2,khjd2,40,100,'normalized','Pd',Pd);
[pk1x,indexx]=max(pxx);
fap_matrix=[pth,Pfa'];  
fit_fap=fit(fap_matrix(:,1),log10(fap_matrix(:,2)),'poly1');
one_hha=max(pxx);
fap_one= feval(fit_fap,one_hha); 
[pxxsel,fsel]=plomb(magconstant,khjd2,1,'normalized');
[pksel,f0sel] = findpeaks(pxxsel,fsel,'minpeakheight',10);
pxxsel1=0.0.*pxxsel+1.0;
for isel=1:length(pksel)
    kisel=find(abs(fsel-f0sel(isel))<0.00001);
    pxx(kisel-1:kisel+1,1)=0.001;
end
halfmaxpxx=max(pxx)*0.5;
[pk,f0] = findpeaks(pxx,f,'minpeakheight',halfmaxpxx);
if max(pk)>0
[pk1,index]=max(pk);
flast=f0(index);
period=1.0/flast;
per(i)=period;
psd(i)=max(pxx);
fap1(i)=fap_one;
d=khjd2./period-fix(khjd2./period);
d1=d+1.0;
d2=[d;d1]; 
kmag3=[kmag2;kmag2];
f2=fittype('a0+a1*cos(2*pi*x)+b1*sin(2*pi*x)+a2*cos(4*pi*x)+b2*sin(4*pi*x)+a3*cos(6*pi*x)+b3*sin(6*pi*x)+a4*cos(8*pi*x)+b4*sin(8*pi*x)+a5*cos(10*pi*x)+b5*sin(10*pi*x)+a6*cos(12*pi*x)+b6*sin(12*pi*x)');

[f1,gof]=fit(d2,kmag3,f2,'StartPoint', [1, 0.001,  0.001,  0.001,  0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]);
coeffs=coeffvalues(f1);
dmy(i)=mean(kmag2);
amp1y(i)=max(f1(d))-min(f1(d));
c3y(i)=gof.adjrsquare;
c4y(i)=gof.rmse;
canmag=kmag2-f1(d);
[pxx2,fx2]=plomb(canmag,khjd2,40,100,'normalized');
[pxx2,fx2,pth2]=plomb(canmag,khjd2,40,100,'normalized','Pd',Pd);
fap_two_matrix=[pth2,Pfa'];
fit_two_fap=fit(fap_two_matrix(:,1),log10(fap_two_matrix(:,2)),'poly1');
halfmaxpxx2=max(pxx2)*0.5;
[pmax2,tto]=max(pxx2);
two_hh=max(pxx2);
fap_two= feval(fit_two_fap,two_hh); 
psd22(i)=pmax2;
p2s(i)=1/fx2(tto);
fap2(i)=fap_two;
[pk2,f02]=findpeaks(pxx2,fx2,'minpeakheight',halfmaxpxx2);
if max(pk2)>0
[pk12,index2]=max(pk2);
flast2=f02(index2);
period2=1.0/flast2;
if abs(period2/period-0.77)>0.03 && abs(period/period2-0.77)>0.03
    y=find(abs(1./f02./period-0.77)<0.03|abs(f02.*period-0.77)<0.03);
    ooy=f02(y);
    oox=pk2(y);
    [cc,dd]=sort(oox);
    if ~isempty(y)
       period2=1/ooy(end);
       pmax2=oox(end);
    end
end     
per2(i)=period2;
period_ratio(i)=period2./period;
psd2(i)=pmax2;
dx=khjd2./period2-fix(khjd2./period2);
dx1=dx+1.0;
dx2=[dx;dx1];
canmag3=[canmag;canmag];
[f2xx,gof2]=fit(dx2,canmag3,f2,'StartPoint', [1, 0.001,  0.001,  0.001,  0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]);
coeffs2=coeffvalues(f2xx);
dmy2(i)=mean(canmag);
amplitude=max(f2xx(dx))-min(f2xx(dx));
amp2y(i)=amplitude;
c3y2(i)=gof2.adjrsquare;
c4y2(i)=gof2.rmse;


if fap_two>-3;

figure(2)
subplot('position',[0.08,0.57,0.40,0.40])
plot(d2,kmag3,'r.','markersize',10);
hold on
plot(ccc3,f1(ccc3),'g','LineWidth',4);
xlim([-0.1 2.1])
ylim('auto')
set(gca,'YDir','reverse');
xlabel('pulsation phase','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('r (mag)','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.08,0.08,0.40,0.40])
plot(f,pxx,'-','LineWidth',2.5)
hold on
plot(f0(index),pk1,'o','MarkerFaceColor',[0.4940 0.1840 0.5560],'MarkerEdgeColor',[0.6350 0.0780 0.1840],'markersize',7)
xlabel('Frequency','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('PSD','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','off')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.57,0.57,0.40,0.40])
plot(dx2,canmag3,'r.','markersize',10);
hold on
plot(ccc3,f2xx(ccc3),'g','LineWidth',4);
xlim([-0.1 2.1])
ylim('auto')
set(gca,'YDir','reverse');
xlabel('pulsation phase','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('\Delta r (mag) ','Interpreter','tex','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.57,0.08,0.40,0.40])
plot(fx2,pxx2,'-','LineWidth',2.5)
hold on
plot(f02(index2),pk12,'o','MarkerFaceColor',[0.4940 0.1840 0.5560],'MarkerEdgeColor',[0.6350 0.0780 0.1840],'markersize',7)
xlabel('Frequency','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('PSD','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off
set(gcf,'OuterPosition',[1,1,950,580], 'position',[1,1,950,580]);

savepath='/Users/qijia/Downloads/jq/6.5/newpsd/fapover3';
fileName = ['ra=' num2str(rax(i)) 'dec=' num2str(decx(i)) '.jpg'];
fullPath = fullfile(savepath, fileName);
saveas(figure(2), fullPath);
close all
end


if fap_two<-3 & amplitude<0.01;
figure(4)
subplot('position',[0.08,0.57,0.40,0.40])
plot(d2,kmag3,'r.','markersize',10);
hold on
plot(ccc3,f1(ccc3),'g','LineWidth',4);
xlim([-0.1 2.1])
ylim('auto')
set(gca,'YDir','reverse');
xlabel('pulsation phase','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('r (mag)','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.08,0.08,0.40,0.40])
plot(f,pxx,'-','LineWidth',2.5)
hold on
plot(f0(index),pk1,'o','MarkerFaceColor',[0.4940 0.1840 0.5560],'MarkerEdgeColor',[0.6350 0.0780 0.1840],'markersize',7)
xlabel('Frequency','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
ylabel('PSD','FontName','Times New Roman','FontSize',18,'FontWeight','bold')
set(gca,'XMinorTick','off')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off

subplot('position',[0.57,0.57,0.40,0.40]);
plot(dx2,canmag3,'r.','markersize',10);
hold on
plot(ccc3,f2xx(ccc3),'g','LineWidth',4);
xlim([-0.1 2.1])
ylim('auto');
set(gca,'YDir','reverse');
xlabel('pulsation phase','FontName','Times New Roman','FontSize',18,'FontWeight','bold');
ylabel('\Delta r (mag) ','Interpreter','tex','FontName','Times New Roman','FontSize',18,'FontWeight','bold');
set(gca,'XMinorTick','on');
set(gca,'YMinorTick','on');
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold');
hold off

subplot('position',[0.57,0.08,0.40,0.40]);
plot(fx2,pxx2,'-','LineWidth',2.5);
hold on
plot(f02(index2),pk12,'o','MarkerFaceColor',[0.4940 0.1840 0.5560],'MarkerEdgeColor',[0.6350 0.0780 0.1840],'markersize',7);
xlabel('Frequency','FontName','Times New Roman','FontSize',18,'FontWeight','bold');
ylabel('PSD','FontName','Times New Roman','FontSize',18,'FontWeight','bold');
set(gca,'XMinorTick','on')
set(gca,'YMinorTick','on')
set(gca,'LineWidth',1)
set(gca,'TickLength',[0.01 0.02]);
set(gca,'FontName','Times New Roman','FontSize',16,'FontWeight','bold')
hold off
set(gcf,'OuterPosition',[1,1,950,580], 'position',[1,1,950,580]);
savepath2='/Users/qijia/Downloads/jq/6.5/newpsd/faploweramplower';
fileName2= ['ra=' num2str(rax(i)) 'dec=' num2str(decx(i)) '.jpg'];
fullPath2 = fullfile(savepath2, fileName2);
saveas(figure(4), fullPath2);
close all


end
end
end
end
nn(i)=i;
end

selkfour_fap=[rax',decx',per',psd',amp1y',dmy',fap1',per2',psd2',amp2y',dmy2',fap2',psd22',p2s',period_ratio'];
save selkfour_fap

datacolumns = {'ra','dec','per','psd','amp1y','mag','fap1','per2','psd2','amp2y','mag2','fap2','psd22','p2s','ratio'};
newtable=table(selkfour_fap(:,1),selkfour_fap(:,2),selkfour_fap(:,3),selkfour_fap(:,4),selkfour_fap(:,5),selkfour_fap(:,6),selkfour_fap(:,7),selkfour_fap(:,8),selkfour_fap(:,9),selkfour_fap(:,10),selkfour_fap(:,11),selkfour_fap(:,12),selkfour_fap(:,13),selkfour_fap(:,14),selkfour_fap(:,15),'VariableNames',datacolumns);
writetable(newtable, 'ansselkfourfap.csv');


%%
trasix=[selkone_fap;selkfour_fap];
fapfind=find(fap2>-3);
dsda=trasix(fapfind,:);
datacolumns = {'ra','dec','per','psd','amp1y','mag','fap1','per2','psd2','amp2y','mag2','fap2','psd22','p2s','ratio'};
newtable=table(dsda(:,1),dsda(:,2),dsda(:,3),dsda(:,4),dsda(:,5),dsda(:,6),dsda(:,7),dsda(:,8),dsda(:,9),dsda(:,10),dsda(:,11),dsda(:,12),dsda(:,13),dsda(:,14),dsda(:,15),'VariableNames',datacolumns);
writetable(newtable, 'fapcondition.csv');

rasda=[selkone_fap;selkfor_fap];
fsdfs=find(fap<-3&amp2y<0.01);
sdawd=rasda(fsdfs,:);
datacolumns = {'ra','dec','per','psd','amp1y','mag','fap1','per2','psd2','amp2y','mag2','fap2','psd22','p2s','ratio'};
newtable=table(sdawd(:,1),sdawd(:,2),sdawd(:,3),sdawd(:,4),sdawd(:,5),sdawd(:,6),sdawd(:,7),sdawd(:,8),sdawd(:,9),sdawd(:,10),sdawd(:,11),sdawd(:,12),sdawd(:,13),sdawd(:,14),sdawd(:,15),'VariableNames',datacolumns);
writetable(newtable, 'fapandampcondition.csv');

fapcombined=[selkone_fap;selkfour_fap];
datacolumns = {'ra','dec','per','psd','amp1y','mag','fap1','per2','psd2','amp2y','mag2','fap2','psd22','p2s','ratio'};
newtable=table(fapcombined(:,1),fapcombined(:,2),fapcombined(:,3),fapcombined(:,4),fapcombined(:,5),fapcombined(:,6),fapcombined(:,7),fapcombined(:,8),fapcombined(:,9),fapcombined(:,10),fapcombined(:,11),fapcombined(:,12),fapcombined(:,13),fapcombined(:,14),fapcombined(:,15),'VariableNames',datacolumns);
writetable(newtable, 'fapcombined.csv');




newda=[selkone_fap;selkfour_fap];
fapfind=find(newda(:,12)>-3);

newda(fapfind,:)=[];
% newda(fsdfs,:)=[];
datacolumns = {'ra','dec','per','psd','amp1y','mag','fap1','per2','psd2','amp2y','mag2','fap2','psd22','p2s','ratio'};
newtable=table(newda(:,1),newda(:,2),newda(:,3),newda(:,4),newda(:,5),newda(:,6),newda(:,7),newda(:,8),newda(:,9),newda(:,10),newda(:,11),newda(:,12),newda(:,13),newda(:,14),newda(:,15),'VariableNames',datacolumns);
writetable(newtable, 'fapflitered.csv');








