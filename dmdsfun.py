import numpy as np
from symfit import parameters, variables, sin, cos, Fit, Variable, Parameter
import matplotlib.pyplot as plt
import pandas as pd
from astropy.timeseries import LombScargle

def fourier1(t, a0, a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6):
    series = a0 + a1*cos(2*np.pi*t)+ b1*sin(2*np.pi*t) + a2*cos(4*np.pi*t) + b2*sin(4*np.pi*t) + a3*cos(6*np.pi*t) + b3*sin(6*np.pi*t) + a4*cos(8*np.pi*t) + b4*sin(8*np.pi*t) + a5*cos(10*np.pi*t) + b5*sin(10*np.pi*t) + a6*cos(12*np.pi*t) + b6*sin(12*np.pi*t)
    return series

def nornal(pn_max,fn,pn):
    threshold1 = 0.8 * pn_max
    indices_greater_than_threshold = np.where(pn > threshold1)[0]
    f_values_greater_than_threshold = fn[indices_greater_than_threshold]
    psd_values_greater_than_threshold = pn[indices_greater_than_threshold]
    grouped_frequencies = []
    grouped_psd_values = []
    current_group = []
    current_psd_values = []
    for i in range(len(f_values_greater_than_threshold)):
        if i == 0 or f_values_greater_than_threshold[i] - f_values_greater_than_threshold[i-1] < 1:
            current_group.append(f_values_greater_than_threshold[i])
            current_psd_values.append(psd_values_greater_than_threshold[i])
        else:
            grouped_frequencies.append(np.mean(current_group))
            grouped_psd_values.append(np.mean(current_psd_values))
            current_group = [f_values_greater_than_threshold[i]]
            current_psd_values = [psd_values_greater_than_threshold[i]]
    grouped_frequencies.append(np.mean(current_group))
    grouped_psd_values.append(np.mean(current_psd_values))
    grouped_frequencies = np.array(grouped_frequencies)
    grouped_psd_values = np.array(grouped_psd_values)
    n=len(grouped_frequencies)
    return n


def first_fun(each_star):
    f1,p1 = LombScargle(each_star.hjd, each_star.mag).autopower(samples_per_peak=100,minimum_frequency=1, maximum_frequency=100)
    index1=1/f1<0.3
    max_p1 =p1[index1].argmax()
    f1_final=f1[index1][max_p1]
    p1_max=p1[index1][max_p1]

    max_psd_index1 = np.argmax(p1)
    max_psd1 = p1[max_psd_index1]
    noise_indices = np.arange(len(p1)) != max_psd_index1
    average_noise = np.mean(p1[noise_indices])
    snr1 = max_psd1 / average_noise

    over_psd1=nornal(p1_max,f1,p1)

    fap1= np.log10(LombScargle(each_star.hjd, each_star.mag).false_alarm_probability(power=p1_max))
    period1 = 1/f1_final
    phase1 = ((each_star.hjd - each_star.hjd[0])/period1)%1 
    t1, y1 = variables('t1, y1')
    model_dict1 = {y1: fourier1(t1, a0=Parameter('a0'), a1=Parameter('a1'), a2=Parameter('a2'), a3=Parameter('a3'), a4=Parameter('a4'),a5=Parameter('a5'),a6=Parameter('a6'),b1=Parameter('b1'), b2=Parameter('b2'), b3=Parameter('b3'), b4=Parameter('b4'),b5=Parameter('b5'),b6=Parameter('b6'))}
    fit1 = Fit(model_dict1, t1=np.array(phase1), y1=np.array(each_star.mag))
    fit_result1 = fit1.execute()
    params = fit_result1.params
    t_fit = np.linspace(np.min(phase1), 2*np.max(phase1), 2000)
    model_values = fit_result1.model(t1=t_fit, **params)
    model_values = np.squeeze(model_values)  
    predict_max = np.max(model_values)
    predict_min = np.min(model_values)
    amplitude1 = predict_max - predict_min
    residual_mag = each_star.mag - fit1.model(t1=phase1, **fit_result1.params).y1
    return p1_max, fap1, f1_final, period1, amplitude1, residual_mag,max_psd1,over_psd1,snr1,f1,p1,phase1,t_fit,model_values


def double_fun(each_star, residual_mag):
    f2, p2 = LombScargle(each_star.hjd, residual_mag).autopower(samples_per_peak=100, minimum_frequency=1, maximum_frequency=100)
    index2=1/f2<0.3
    max_p2 =p2[index2].argmax()
    f2_final=f2[index2][max_p2]
    p2_max=p2[index2][max_p2]

    max_psd_index2 = np.argmax(p2)
    max_psd2 = p2[max_psd_index2]
    noise_indices = np.arange(len(p2)) != max_psd_index2
    average_noise = np.mean(p2[noise_indices])
    snr2 = max_psd2 / average_noise
    # threshold2 = 0.95 * p2_max
    # num_greater_than_threshold2 = sum(p2 > threshold2)

    over_psd2=nornal(p2_max,f2,p2)


    fap2 = np.log10(LombScargle(each_star.hjd, residual_mag).false_alarm_probability(power=p2_max))
    period2 = 1/f2_final
    phase2 = ((each_star.hjd - each_star.hjd[0])/period2) % 1 
    t2, y2 = variables('t2, y2')
    model_dict2 = {y2: fourier1(t2, a0=Parameter('a0'), a1=Parameter('a1'), a2=Parameter('a2'), a3=Parameter('a3'), a4=Parameter('a4'),a5=Parameter('a5'),a6=Parameter('a6'),b1=Parameter('b1'), b2=Parameter('b2'), b3=Parameter('b3'), b4=Parameter('b4'),b5=Parameter('b5'),b6=Parameter('b6'))}
    fit2 = Fit(model_dict2, t2=np.array(phase2), y2=np.array(residual_mag))
    fit_result2 = fit2.execute()
    params2 = fit_result2.params
    t_fit2 = np.linspace(np.min(phase2), 2*np.max(phase2), 2000)
    model_values2 = fit_result2.model(t2=t_fit2, **params2)
    model_values2 = np.squeeze(model_values2)  
    predict_max2 = np.max(model_values2)
    predict_min2 = np.min(model_values2)
    amplitude2 = predict_max2 - predict_min2
    residual_mag2 = residual_mag - fit2.model(t2=phase2, **fit_result2.params).y2
    return p2_max, fap2, f2_final, period2, amplitude2, residual_mag2,max_psd2,over_psd2,snr2,f2,p2,phase2,t_fit2,model_values2



def tripe_fun(each_star, residual_mag2):
    f3, p3 = LombScargle(each_star.hjd, residual_mag2).autopower(samples_per_peak=100,minimum_frequency=1, maximum_frequency=100)

    index3=1/f3<0.3
    max_p3 =p3[index3].argmax()
    f3_final=f3[index3][max_p3]
    p3_max=p3[index3][max_p3]

    max_psd_index3 = np.argmax(p3)
    max_psd3 = p3[max_psd_index3]
    noise_indices = np.arange(len(p3)) != max_psd_index3
    average_noise = np.mean(p3[noise_indices])
    snr3 = max_psd3 / average_noise
    # threshold3 = 0.95 * p3_max
    # num_greater_than_threshold3 = sum(p3 > threshold3)
    over_psd3=nornal(p3_max,f3,p3)


    fap3 = np.log10(LombScargle(each_star.hjd, residual_mag2).false_alarm_probability(power=p3_max))
    period3 = 1/f3_final
    phase3 = ((each_star.hjd - each_star.hjd[0])/period3)%1 
    t3, y3 = variables('t3, y3')
    model_dict3 = {y3: fourier1(t3, a0=Parameter('a0'), a1=Parameter('a1'), a2=Parameter('a2'), a3=Parameter('a3'), a4=Parameter('a4'),a5=Parameter('a5'),a6=Parameter('a6'),b1=Parameter('b1'), b2=Parameter('b2'), b3=Parameter('b3'), b4=Parameter('b4'),b5=Parameter('b5'),b6=Parameter('b6'))}
    fit3 = Fit(model_dict3, t3=np.array(phase3), y3=np.array(residual_mag2))
    fit_result3 = fit3.execute()
    params3 = fit_result3.params
    t_fit3 = np.linspace(np.min(phase3), 2*np.max(phase3), 2000)
    model_values3 = fit_result3.model(t3=t_fit3, **params3)
    model_values3 = np.squeeze(model_values3)  
    predict_max3 = np.max(model_values3)
    predict_min3 = np.min(model_values3)
    amplitude3 = predict_max3 - predict_min3
    residual_mag3 = residual_mag2 - fit3.model(t3=phase3, **fit_result3.params).y3
    return p3_max, fap3, f3_final, period3, amplitude3, residual_mag3, max_psd3, over_psd3, snr3, f3,p3,phase3,t_fit3,model_values3




def fourth_fun(each_star, residual_mag3):
    f4, p4 = LombScargle(each_star.hjd, residual_mag3).autopower(samples_per_peak=100, minimum_frequency=1, maximum_frequency=100)
    index4=1/f4<0.3
    max_p4 =p4[index4].argmax()
    f4_final=f4[index4][max_p4]
    p4_max=p4[index4][max_p4]

    max_psd_index4 = np.argmax(p4)
    max_psd4 = p4[max_psd_index4]
    noise_indices = np.arange(len(p4)) != max_psd_index4
    average_noise = np.mean(p4[noise_indices])
    snr4 = max_psd4 / average_noise
    # threshold4 = 0.95 * p4_max
    # num_greater_than_threshold4 = sum(p4 > threshold4)
    over_psd4=nornal(p4_max,f4,p4)

    fap4 = np.log10(LombScargle(each_star.hjd, residual_mag3).false_alarm_probability(power=p4_max))
    period4 = 1/f4_final
    phase4 = ((each_star.hjd - each_star.hjd[0])/period4)%1 
    t4, y4 = variables('t4, y4')
    model_dict4 = {y4: fourier1(t4, a0=Parameter('a0'), a1=Parameter('a1'), a2=Parameter('a2'), a3=Parameter('a3'), a4=Parameter('a4'),a5=Parameter('a5'),a6=Parameter('a6'),b1=Parameter('b1'), b2=Parameter('b2'), b3=Parameter('b3'), b4=Parameter('b4'),b5=Parameter('b5'),b6=Parameter('b6'))}
    fit4 = Fit(model_dict4, t4=np.array(phase4), y4=np.array(residual_mag3))
    fit_result4 = fit4.execute()
    params4 = fit_result4.params
    t_fit4 = np.linspace(np.min(phase4), 2*np.max(phase4), 2000)
    model_values4 = fit_result4.model(t4=t_fit4, **params4)
    model_values4 = np.squeeze(model_values4)  
    predict_max4 = np.max(model_values4)
    predict_min4 = np.min(model_values4)
    amplitude4 = predict_max4 - predict_min4
    residual_mag4 = residual_mag3 - fit4.model(t4=phase4, **fit_result4.params).y4
    return p4_max, fap4,f4_final, period4, amplitude4, residual_mag4, max_psd4, over_psd4, snr4, f4,p4,phase4,t_fit4,model_values4



def fiveth_fun(each_star, residual_mag4):
    f5, p5 = LombScargle(each_star.hjd, residual_mag4).autopower(samples_per_peak=100, minimum_frequency=1, maximum_frequency=100)
    index5=1/f5<0.3
    max_p5 =p5[index5].argmax()
    f5_final=f5[index5][max_p5]
    p5_max=p5[index5][max_p5]

    max_psd_index5 = np.argmax(p5)
    max_psd5 = p5[max_psd_index5]
    noise_indices = np.arange(len(p5)) != max_psd_index5
    average_noise = np.mean(p5[noise_indices])
    snr5 = max_psd5 / average_noise
    # threshold5 = 0.95 * p5_max
    # num_greater_than_threshold5 = sum(p5 > threshold5)
    over_psd5=nornal(p5_max,f5,p5)

    fap5 = np.log10(LombScargle(each_star.hjd, residual_mag4).false_alarm_probability(power=p5_max))
    period5 = 1/f5_final
    phase5 = ((each_star.hjd - each_star.hjd[0])/period5) % 1
    t5, y5 = variables('t5, y5')
    model_dict5 = {y5: fourier1(t5, a0=Parameter('a0'), a1=Parameter('a1'), a2=Parameter('a2'), a3=Parameter('a3'), a4=Parameter('a4'),a5=Parameter('a5'),a6=Parameter('a6'),b1=Parameter('b1'), b2=Parameter('b2'), b3=Parameter('b3'), b4=Parameter('b4'),b5=Parameter('b5'),b6=Parameter('b6'))}
    fit5 = Fit(model_dict5, t5=np.array(phase5), y5=np.array(residual_mag4))
    fit_result5 = fit5.execute()
    params5 = fit_result5.params
    t_fit5 = np.linspace(np.min(phase5), 2*np.max(phase5), 2000)
    model_values5 = fit_result5.model(t5=t_fit5, **params5)
    model_values5 = np.squeeze(model_values5)  
    predict_max5 = np.max(model_values5)
    predict_min5 = np.min(model_values5)
    amplitude5 = predict_max5 - predict_min5
    residual_mag5 = residual_mag4 - fit5.model(t5=phase5, **fit_result5.params).y5
    return p5_max, fap5,f5_final, period5, amplitude5, residual_mag5, max_psd5, over_psd5, snr5,f5,p5,phase5,t_fit5,model_values5



def sixth_fun(each_star, residual_mag5):
    f6, p6 = LombScargle(each_star.hjd, residual_mag5).autopower(samples_per_peak=100, minimum_frequency=1, maximum_frequency=100)
    index6=1/f6<0.3
    max_p6 =p6[index6].argmax()
    f6_final=f6[index6][max_p6]
    p6_max=p6[index6][max_p6]

    max_psd_index6 = np.argmax(p6)
    max_psd6 = p6[max_psd_index6]
    noise_indices = np.arange(len(p6)) != max_psd_index6
    average_noise = np.mean(p6[noise_indices])
    snr6 = max_psd6 / average_noise
    # threshold6 = 0.95 * p6_max
    # num_greater_than_threshold6 = sum(p6 > threshold6)
    over_psd6=nornal(p6_max,f6,p6)

    fap6 = np.log10(LombScargle(each_star.hjd, residual_mag5).false_alarm_probability(power=p6_max))
    period6 = 1/f6_final
    phase6 = ((each_star.hjd - each_star.hjd[0])/period6) % 1
    t6, y6 = variables('t6, y6')
    model_dict6 = {y6: fourier1(t6, a0=Parameter('a0'), a1=Parameter('a1'), a2=Parameter('a2'), a3=Parameter('a3'), a4=Parameter('a4'),a5=Parameter('a5'),a6=Parameter('a6'),b1=Parameter('b1'), b2=Parameter('b2'), b3=Parameter('b3'), b4=Parameter('b4'),b5=Parameter('b5'),b6=Parameter('b6'))}
    fit6 = Fit(model_dict6, t6=np.array(phase6), y6=np.array(residual_mag5))
    fit_result6 = fit6.execute()
    params6 = fit_result6.params
    t_fit6 = np.linspace(np.min(phase6), 2*np.max(phase6), 2000)
    model_values6 = fit_result6.model(t6=t_fit6, **params6)
    model_values6 = np.squeeze(model_values6)  
    predict_max6 = np.max(model_values6)
    predict_min6 = np.min(model_values6)
    amplitude6 = predict_max6 - predict_min6
    return p6_max, fap6,f6_final, period6, amplitude6, max_psd6, over_psd6, snr6,f6,p6,phase6,t_fit6,model_values6




