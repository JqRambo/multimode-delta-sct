import pandas as pd
from astropy.io import fits
import dmdsfun as dn
import numpy as np
import os
from tqdm import tqdm

def process_files(csv_file_name, fits_file_name):

    all_data=pd.DataFrame(columns=['control_id','source','ra','dec',
                                        'mean_originmag','std_originmag','mean_originmagerr','filtered_meanmag','filtered_meanmagerr',
                                        'period1','psd1','f1_final','fap1','amp1',
                                        'period2','psd2','f2_final','fap2','amp2',
                                        'period3','psd3','f3_final','fap3','amp3',
                                        'period4','psd4','f4_final','fap4','amp4',
                                        'period5','psd5','f5_final','fap5','amp5',
                                        'period6','psd6','f6_final','fap6','amp6','filtercode'])
    hdulist = fits.open(fits_file_name)
    fitsdata = hdulist[1].data
    oidtest = pd.read_csv(csv_file_name)
    oidtest = oidtest[oidtest.filtercode == 'zg']
    max_contro_o1 = oidtest['cntr_01'].max()    
    for i in tqdm(range(max_contro_o1+1)):
    # for i in tqdm(range(101)):
        subset = oidtest[oidtest['cntr_01'] == i]
        if len(subset)>0:
            control_id = subset.cntr_01.iloc[0]
            oid_list = subset.oid.values.tolist()
            unfiltered = fitsdata[np.isin(fitsdata.oid, oid_list) & (fitsdata.catflags < 30000)& (fitsdata.filtercode=='zg')]        
            if len(unfiltered)>30:               
                source = unfiltered.oid[1]
                filter_code=unfiltered.filtercode[0]
                ra = np.mean(unfiltered.ra)
                dec = np.mean(unfiltered.dec)
                mean_originmag=np.mean(unfiltered.mag)
                std_originmag = np.std(unfiltered.mag)
                mean_originmagerr=np.mean(unfiltered.magerr)
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
                filtered_meanmag=np.mean(each_star.mag)
                filtered_meanmagerr=np.mean(each_star.magerr)

                p1_max, fap1, f1_final, period1, amplitude1, residual_mag,max_psd1,over_psd1,snr1,f1,p1,phase1,t_fit,model_values=dn.first_fun(each_star)
                p2_max, fap2, f2_final, period2, amplitude2, residual_mag2,max_psd2,over_psd2,snr2,f2,p2,phase2,t_fit2,model_values2=dn.double_fun(each_star, residual_mag)
                
                if fap2>-3 or amplitude2<0.01 or p2_max<0.1 or max_psd2>p2_max or snr2<30 or over_psd2>=3:
                    pass
                else:
                    p3_max, fap3, f3_final, period3, amplitude3, residual_mag3, max_psd3, over_psd3, snr3, f3,p3,phase3,t_fit3,model_values3=dn.tripe_fun(each_star, residual_mag2)
                    
                    if fap3>-3 or amplitude3<0.01 or p3_max<0.1 or max_psd3>p3_max or snr3<30 or over_psd3>=3:
                        all_data=pd.concat([all_data, pd.DataFrame({'control_id':control_id,'source':source,'ra':ra,'dec':dec,
        'mean_originmag':mean_originmag,'std_originmag':std_originmag,'mean_originmagerr':mean_originmagerr,'filtered_meanmag':filtered_meanmag,'filtered_meanmagerr':filtered_meanmagerr,
                'period1':period1,'psd1':p1_max,'f1_final':f1_final,'fap1':fap1,'amp1':amplitude1,
                'period2':period2,'psd2':p2_max,'f2_final':f2_final,'fap2':fap2,'amp2':amplitude2,
                'period3':0,'psd3':0,'f3_final':0,'fap3':0,'amp3':0,
                'period4':0,'psd4':0,'f4_final':0,'fap4':0,'amp4':0,
                'period5':0,'psd5':0,'f5_final':0,'fap5':0,'amp5':0,
                'period6':0,'psd6':0,'f6_final':0,'fap6':0,'amp6':0,'filtercode':filter_code}, index=[0])], ignore_index=True)
                    
                    else:
                        p4_max, fap4,f4_final, period4, amplitude4, residual_mag4, max_psd4, over_psd4, snr4, f4,p4,phase4,t_fit4,model_values4=dn.fourth_fun(each_star, residual_mag3)

                        if fap4>-3 or amplitude4<0.01 or p4_max<0.1 or max_psd4>p4_max or snr4<30 or over_psd4>=3:
                            all_data=pd.concat([all_data, pd.DataFrame({'control_id':control_id,'source':source,'ra':ra,'dec':dec,
                                                                    'mean_originmag':mean_originmag,'std_originmag':std_originmag,'mean_originmagerr':mean_originmagerr,'filtered_meanmag':filtered_meanmag,'filtered_meanmagerr':filtered_meanmagerr,
                                                                    'period1':period1,'psd1':p1_max,'f1_final':f1_final,'fap1':fap1,'amp1':amplitude1,
                                                                    'period2':period2,'psd2':p2_max,'f2_final':f2_final,'fap2':fap2,'amp2':amplitude2,
                                                                    'period3':period3,'psd3':p3_max,'f3_final':f3_final,'fap3':fap3,'amp3':amplitude3,
                                                                    'period4':0,'psd4':0,'f4_final':0,'fap4':0,'amp4':0,
                                                                    'period5':0,'psd5':0,'f5_final':0,'fap5':0,'amp5':0,
                                                                    'period6':0,'psd6':0,'f6_final':0,'fap6':0,'amp6':0,'filtercode':filter_code}, index=[0])], ignore_index=True)
                    

                        else:
                            p5_max, fap5,f5_final, period5, amplitude5, residual_mag5, max_psd5, over_psd5, snr5,f5,p5,phase5,t_fit5,model_values5=dn.fiveth_fun(each_star, residual_mag4)                  
                            if fap5>-3 or amplitude5<0.01 or p5_max<0.1 or max_psd5>p5_max or snr5<30 or over_psd5>=3:
                                all_data=pd.concat([all_data, pd.DataFrame({'control_id':control_id,'source':source,'ra':ra,'dec':dec,
                                                            'mean_originmag':mean_originmag,'std_originmag':std_originmag,'mean_originmagerr':mean_originmagerr,'filtered_meanmag':filtered_meanmag,'filtered_meanmagerr':filtered_meanmagerr,
                                                            'period1':period1,'psd1':p1_max, 'f1_final':f1_final,'fap1':fap1,'amp1':amplitude1,
                                                            'period2':period2,'psd2':p2_max, 'f2_final':f2_final,'fap2':fap2,'amp2':amplitude2,
                                                            'period3':period3,'psd3':p3_max, 'f3_final':f3_final,'fap3':fap3,'amp3':amplitude3,
                                                            'period4':period4,'psd4':p4_max, 'f4_final':f4_final,'fap4':fap4,'amp4':amplitude4,
                                                            'period5':0,'psd5':0,'f5_final':0,'fap5':0,'amp5':0,
                                                            'period6':0,'psd6':0,'f6_final':0,'fap6':0,'amp6':0,'filtercode':filter_code}, index=[0])], ignore_index=True)

                            else:
                                p6_max, fap6,f6_final, period6, amplitude6, residual_mag6, max_psd6, over_psd6, snr6,f6,p6,phase6,t_fit6,model_values6=dn.fiveth_fun(each_star, residual_mag5)                  
                                if fap6>-3 or amplitude6<0.01 or p6_max<0.1 or max_psd6>p6_max or snr6<30 or over_psd6>=3:
                                    all_data=pd.concat([all_data, pd.DataFrame({'control_id':control_id,'source':source,'ra':ra,'dec':dec,
                                                                'mean_originmag':mean_originmag,'std_originmag':std_originmag,'mean_originmagerr':mean_originmagerr,'filtered_meanmag':filtered_meanmag,'filtered_meanmagerr':filtered_meanmagerr,
                                                                'period1':period1,'psd1':p1_max,'f1_final':f1_final,'fap1':fap1,'amp1':amplitude1,
                                                                'period2':period2,'psd2':p2_max,'f2_final':f2_final,'fap2':fap2,'amp2':amplitude2,
                                                                'period3':period3,'psd3':p3_max,'f3_final':f3_final,'fap3':fap3,'amp3':amplitude3,
                                                                'period4':period4,'psd4':p4_max,'f4_final':f4_final,'fap4':fap4,'amp4':amplitude4,
                                                                'period5':period5,'psd4':p5_max,'f5_final':f5_final,'fap5':fap5,'amp5':amplitude5,
                                                                'period6':0,'psd6':0,'f6_final':0,'fap6':0,'amp6':0,'filtercode':filter_code}, index=[0])], ignore_index=True)  
                                else:
                                    all_data=pd.concat([all_data, pd.DataFrame({'control_id':control_id,'source':source,'ra':ra,'dec':dec,
                                                            'mean_originmag':mean_originmag,'std_originmag':std_originmag,'mean_originmagerr':mean_originmagerr,'filtered_meanmag':filtered_meanmag,'filtered_meanmagerr':filtered_meanmagerr,
                                                            'period1':period1,'psd1':p1_max,'f1_final':f1_final,'fap1':fap1,'amp1':amplitude1,
                                                            'period2':period2,'psd2':p2_max,'f2_final':f2_final,'fap2':fap2,'amp2':amplitude2,
                                                            'period3':period3,'psd3':p3_max,'f3_final':f3_final,'fap3':fap3,'amp3':amplitude3,
                                                            'period4':period4,'psd4':p4_max,'f4_final':f4_final,'fap4':fap4,'amp4':amplitude4,
                                                            'period5':period5,'psd5':p5_max,'f5_final':f5_final,'fap5':fap5,'amp5':amplitude5,
                                                            'period6':period6,'psd6':p6_max,'f6_final':f6_final,'fap6':fap6,'amp6':amplitude6,'filtercode':filter_code}, index=[0])], ignore_index=True) 
                                    

    return all_data


if __name__ == '__main__':
    file_path = '/Users/qijia/Downloads/dmdsdr20/g/'
    file_list = os.listdir(file_path)
    for i in range(1,4):
        csv_file_name = f"g{i}.csv"
        fits_file_name = f"g{i}.fits"
        csv_file_path = os.path.join(file_path, csv_file_name)
        fits_file_path = os.path.join(file_path, fits_file_name)
        kksd=process_files(csv_file_path, fits_file_name)
        save_path=os.path.join(file_path,f'ng{i}.csv')
        kksd.to_csv(save_path,index=False)






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

