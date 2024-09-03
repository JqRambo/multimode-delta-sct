import pandas as pd
from astropy.io import fits
import dmdsfun as dn
import numpy as np
import os
from tqdm import tqdm
import mode_figure_fun as mfg

def process_files(csv_file_name, fits_file_name):

    hdulist = fits.open(fits_file_name)
    fitsdata = hdulist[1].data
    oidtest = pd.read_csv(csv_file_name)
    # oidtest = oidtest[oidtest.filtercode == 'zr']
    # max_contro_o1 = oidtest['cntr_01'].max()    
    # for i in tqdm(range(max_contro_o1+1)):
    for i in tqdm(range(1,101)):
        subset = oidtest[oidtest['cntr_01'] == i]
        if len(subset)>0:
            control_id = subset.cntr_01.iloc[0]
            oid_list = subset.oid.values.tolist()
            unfiltered = fitsdata[np.isin(fitsdata.oid, oid_list) & (fitsdata.catflags < 30000)& (fitsdata.filtercode=='zr')]        
            if len(unfiltered)>30:               
                source = unfiltered.oid[1]
                filter_code=unfiltered.filtercode[0]
                lable_str=filter_code[1]
                ra = np.mean(unfiltered.ra)
                dec = np.mean(unfiltered.dec)

                mu=np.median(unfiltered.mag)
                unfiltered=unfiltered[np.abs(unfiltered.mag-mu)<2]
                std1=np.std(unfiltered.mag)
                mu2=np.median(unfiltered.mag)
                unfiltered = unfiltered[np.abs(unfiltered.mag-mu2)<3*std1]
                time=unfiltered['hjd'].astype('<f8')
                mag=unfiltered['mag'].astype('<f8')
                mge=unfiltered['magerr'].astype('<f8')
                df = pd.DataFrame({'hjd': time, 'mag': mag, 'magerr': mge})
                sort_idx = np.argsort(df.hjd)
                df = df.iloc[sort_idx]  
                sort_hjd = df.hjd
                sort_mag = df.mag
                sort_mge = df.magerr
                aa, tb = np.unique(sort_hjd, return_inverse=True)
                khjd2 = sort_hjd[np.isin(np.arange(len(sort_hjd)), tb)]
                kmag2 = sort_mag[np.isin(np.arange(len(sort_mag)), tb)]
                kmge2 = sort_mge[np.isin(np.arange(len(sort_mge)), tb)]
                df2=pd.DataFrame({'hjd':khjd2,'mag':kmag2,'magerr':kmge2})
                df2['hjd_diff']=df2['hjd'].diff().fillna(df2['hjd'])
                to_remove = df2['hjd_diff']<=0.001
                df_filtered=df2[~to_remove]
                df_filtered = df_filtered.dropna(subset=['hjd'])
                each_star=df_filtered.to_records(index=False)
                p1_max, fap1, f1_final, period1, amplitude1, residual_mag,max_psd1,over_psd1,snr1,f1,p1,phase1,t_fit,model_values=dn.first_fun(each_star)
                p2_max, fap2, f2_final, period2, amplitude2, residual_mag2,max_psd2,over_psd2,snr2,f2,p2,phase2,t_fit2,model_values2=dn.double_fun(each_star, residual_mag)
                
                if fap2>-3 or amplitude2<0.01 or p2_max<0.1 or max_psd2>p2_max or snr2<20 or over_psd2>=3:
                    pass
                else:
                    p3_max, fap3, f3_final, period3, amplitude3, residual_mag3, max_psd3, over_psd3, snr3, f3,p3,phase3,t_fit3,model_values3=dn.tripe_fun(each_star, residual_mag2)
                    if fap3>-3 or amplitude3<0.01 or p3_max<0.1 or max_psd3>p3_max or snr3<20 or over_psd3>=3:
                        mfg.plot_double(source,ra, dec,
            f1, p1, period1, snr1, f1_final, p1_max, phase1, each_star, t_fit, model_values,
            f2, p2, period2, snr2, f2_final, p2_max, phase2, t_fit2, model_values2, residual_mag,lable_str)
                    else:
                        p4_max, fap4,f4_final, period4, amplitude4, residual_mag4, max_psd4, over_psd4, snr4, f4,p4,phase4,t_fit4,model_values4=dn.fourth_fun(each_star, residual_mag3)
                        if fap4>-3 or amplitude4<0.01 or p4_max<0.1 or max_psd4>p4_max or snr4<20 or over_psd4>=3:
                            mfg.plot_triple(source,ra, dec,
            f1, p1, period1, snr1, f1_final, p1_max, phase1, each_star, t_fit, model_values,
            f2, p2, period2, snr2, f2_final, p2_max, phase2, t_fit2, model_values2, residual_mag,
            f3, p3, period3, snr3, f3_final, p3_max, phase3, t_fit3, model_values3, residual_mag2,lable_str)
                        else:
                            p5_max, fap5,f5_final, period5, amplitude5, residual_mag5, max_psd5, over_psd5, snr5,f5,p5,phase5,t_fit5,model_values5=dn.fiveth_fun(each_star, residual_mag4)                  
                            if fap5>-3 or amplitude5<0.01 or p5_max<0.1 or max_psd5>p5_max or snr5<20 or over_psd5>=3:
                                mfg.plot_fourth(source,ra, dec,
            f1, p1, period1, snr1, f1_final, p1_max, phase1, each_star, t_fit, model_values,
            f2, p2, period2, snr2, f2_final, p2_max, phase2, t_fit2, model_values2, residual_mag,
            f3, p3, period3, snr3, f3_final, p3_max, phase3, t_fit3, model_values3, residual_mag2,
            f4, p4, period4, snr4, f4_final, p4_max, phase4, t_fit4, model_values4, residual_mag3,lable_str)
                            else:
                                pass

if __name__ == '__main__':
    file_path = '/Users/qijia/Downloads/dmdsdr20/r/'
    file_list = os.listdir(file_path)
    for i in range(3,4):
        csv_file_name = f"r{i}.csv"
        fits_file_name = f"r{i}.fits"
        csv_file_path = os.path.join(file_path, csv_file_name)
        fits_file_path = os.path.join(file_path, fits_file_name)
        process_files(csv_file_path, fits_file_name)






# if __name__ == '__main__':
#     file_path = '/Users/qijia/Downloads/dr20/'
#     file_list = os.listdir(file_path)
#     all_datas = []
#     for i in range(1, 2):
#         csv_file_name = f"{i}.csv"
#         fits_file_name = f"{i}.fits"
#         csv_file_path = os.path.join(file_path, csv_file_name)
#         fits_file_path = os.path.join(file_path, fits_file_name)
#         kksd = mf.process_files(csv_file_path, fits_file_name)
#         all_datas.append(kksd)
#     data = pd.concat(all_datas, axis=0)
#     name = 'rdata.csv'
#     data.to_csv(file_path + name, index=False)

