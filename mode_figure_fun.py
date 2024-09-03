
import numpy as np
from symfit import parameters, variables, sin, cos, Fit, Variable, Parameter
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import MultipleLocator
import pandas as pd
from astropy.timeseries import LombScargle




def plot_double(source,ra, dec,
            f1, p1, period1, snr1, f1_final, p1_max, phase1, each_star, t_fit, model_values,
            f2, p2, period2, snr2, f2_final, p2_max, phase2, t_fit2, model_values2, residual_mag,lable_str):
    
        fig, axs = plt.subplots(2, 2, figsize=(10, 6), dpi=300)
        axs[0, 0].scatter(f1_final, p1_max, marker='o', color='r', s=20, alpha=1)
        axs[0, 0].plot(f1, p1, color='b', linestyle='-', linewidth=1.0)
        axs[0, 0].text(0.9, 0.95, f"ZTF {source}", transform=axs[0, 0].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
        axs[0, 0].set_xlabel('Frequency', fontsize=6, color='k')
        axs[0, 0].set_ylabel('PSD', fontsize=6, color='k')
        axs[0, 0].xaxis.set_minor_locator(MultipleLocator(5))  
        axs[0, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
        axs[0, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
        axs[0, 0].tick_params(axis='both', labelsize=7)
        axs[0, 0].set_xlim(0,40) 
        axs[0, 0].set_ylim(0, None) 
        
        axs[0, 1].scatter(phase1, each_star.mag, color='r',s=1,alpha=0.7)
        axs[0, 1].scatter([p+1 for p in phase1], each_star.mag, color='r',s=1,alpha=0.7) 
        axs[0, 1].plot(t_fit, model_values, 'g-', alpha=1, label='Fit', linewidth=2, zorder=2) 
        axs[0, 1].text(0.9, 0.95, f"Period = {period1:.8f} [day]\n Mode={snr1}", transform=axs[0, 1].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
        axs[0, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
        axs[0, 1].set_ylabel(f'${lable_str}$ (mag)', fontsize=6, color='k')
        axs[0, 1].xaxis.set_minor_locator(MultipleLocator(0.25))  
        axs[0, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
        axs[0, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
        axs[0, 1].tick_params(axis='both', labelsize=7)
        axs[0, 1].invert_yaxis()


        axs[1, 0].scatter(f2_final, p2_max, marker='o', color='r', s=20, alpha=1)
        axs[1, 0].plot(f2, p2, color='b', linestyle='-', linewidth=1.0)    
        axs[1, 0].set_xlabel('Frequency', fontsize=6, color='k')
        axs[1, 0].set_ylabel('PSD', fontsize=6, color='k')
        axs[1, 0].xaxis.set_minor_locator(MultipleLocator(5))  
        axs[1, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
        axs[1, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
        axs[1, 0].tick_params(axis='both', labelsize=7)
        axs[1, 0].set_xlim(0, 40) 
        axs[1, 0].set_ylim(0, None) 

        axs[1, 1].scatter(phase2, residual_mag, c='r', s=1)
        axs[1, 1].scatter([p+1 for p in phase2], residual_mag, c='r', s=1)
        axs[1 ,1].plot(t_fit2, model_values2, 'g-', alpha=1, label='Fit', linewidth=2, zorder=2) # 增加拟合线的线宽度
        axs[1, 1].text(0.9, 0.95, f"Period = {period2:.8f} [day]\n Mode={snr2}", transform=axs[1, 1].transAxes, fontsize=8,fontweight='normal', va='top', ha='right', color='k')
        axs[1, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
        axs[1, 1].set_ylabel(f'$\Delta {lable_str}$ (mag)', fontsize=6, color='k')
        axs[1, 1].xaxis.set_minor_locator(MultipleLocator(5))  
        axs[1, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
        axs[1, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
        axs[1, 1].tick_params(axis='both', labelsize=7)
        axs[1, 1].invert_yaxis()

        fileName = f"ra={ra},dec={dec}.png"
        savepath2 = '/Users/qijia/Downloads/dmdsdr20/r/fig_test/2f/'
        fullPath = os.path.join(savepath2, fileName)
        plt.savefig(fullPath, format='png', dpi=300)
        
        plt.close() 











def plot_triple(source,ra, dec,
            f1, p1, period1, snr1, f1_final, p1_max, phase1, each_star, t_fit, model_values,
            f2, p2, period2, snr2, f2_final, p2_max, phase2, t_fit2, model_values2, residual_mag,
            f3, p3, period3, snr3, f3_final, p3_max, phase3, t_fit3, model_values3, residual_mag2,lable_str):
    
    

    fig, axs = plt.subplots(3, 2, figsize=(10, 9), dpi=300)
    
    axs[0, 0].scatter(f1_final, p1_max, marker='o', color='r', s=20, alpha=1)
    axs[0, 0].plot(f1, p1, color='b', linestyle='-', linewidth=1.0)
    axs[0, 0].text(0.9, 0.95, f"ZTF {source}", transform=axs[0, 0].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[0, 0].set_xlabel('Frequency', fontsize=6, color='k')
    axs[0, 0].set_ylabel('PSD', fontsize=6, color='k')
    axs[0, 0].xaxis.set_minor_locator(MultipleLocator(5))  
    axs[0, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[0, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[0, 0].tick_params(axis='both', labelsize=7)
    axs[0, 0].set_xlim(0,40) 
    axs[0, 0].set_ylim(0, None) 


    axs[0, 1].scatter(phase1, each_star.mag, color='r',s=1,alpha=0.7)
    axs[0, 1].scatter([p+1 for p in phase1], each_star.mag, color='r',s=1,alpha=0.7) 
    axs[0, 1].plot(t_fit, model_values, 'g-', alpha=1, label='Fit', linewidth=2, zorder=2) 
    axs[0, 1].text(0.9, 0.95, f"Period = {period1:.8f} [day]\n Mode={snr1}", transform=axs[0, 1].transAxes, fontsize=8,  fontweight='normal', va='top', ha='right', color='k')
    axs[0, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
    axs[0, 1].set_ylabel(f'${lable_str}$ (mag)', fontsize=6, color='k')
    axs[0, 1].xaxis.set_minor_locator(MultipleLocator(0.25))  
    axs[0, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[0, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[0, 1].tick_params(axis='both', labelsize=7)
    axs[0, 1].set_ylim(min(each_star.mag)-0.15,None) 
    axs[0, 1].invert_yaxis()



    axs[1, 0].scatter(f2_final, p2_max, marker='o', color='r', s=20, alpha=1)
    axs[1, 0].plot(f2, p2, color='b', linestyle='-', linewidth=1.0)    
    axs[1, 0].text(0.9, 0.95, f"Max_psd={p2_max}", transform=axs[1, 0].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[1, 0].set_xlabel('Frequency', fontsize=6, color='k')
    axs[1, 0].set_ylabel('PSD', fontsize=6, color='k')
    axs[1, 0].xaxis.set_minor_locator(MultipleLocator(5))  
    axs[1, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
    axs[1, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
    axs[1, 0].tick_params(axis='both', labelsize=7)
    axs[1, 0].set_xlim(0, 40) 
    axs[1, 0].set_ylim(0, None) 

    axs[1, 1].scatter(phase2, residual_mag, c='r', s=1)
    axs[1, 1].scatter([p+1 for p in phase2], residual_mag, c='r', s=1)
    axs[1 ,1].plot(t_fit2, model_values2, 'g-', alpha=1, label='Fit', linewidth=2, zorder=2) # 增加拟合线的线宽度
    axs[1, 1].text(0.9, 0.95, f"Period = {period2:.8f} [day]\n Mode={snr2}", transform=axs[1, 1].transAxes, fontsize=8,fontweight='normal', va='top', ha='right', color='k')
    axs[1, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
    axs[1, 1].set_ylabel(f'$\Delta {lable_str}$ (mag)', fontsize=6, color='k')
    axs[1, 1].xaxis.set_minor_locator(MultipleLocator(5))  
    axs[1, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
    axs[1, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
    axs[1, 1].tick_params(axis='both', labelsize=7)
    axs[1, 1].invert_yaxis()
    

    axs[2, 0].scatter(f3_final, p3_max, marker='o', color='r', s=20, alpha=1)
    axs[2, 0].plot(f3, p3, color='b', linestyle='-', linewidth=1.0)    
    axs[2, 0].text(0.9, 0.95, f"\nMax_psd={p3_max}", transform=axs[2, 0].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[2, 0].set_xlabel('Frequency', fontsize=6, color='k')
    axs[2, 0].set_ylabel('PSD', fontsize=6, color='k')
    axs[2, 0].xaxis.set_minor_locator(MultipleLocator(0.25))  
    axs[2, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[2, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[2, 0].tick_params(axis='both', labelsize=7)
    axs[2, 0].set_xlim(0,40) 
    axs[2, 0].set_ylim(0,None) 

    axs[2, 1].scatter(phase3, residual_mag2, c='r', s=1)
    axs[2, 1].scatter([p+1 for p in phase3], residual_mag2, c='r', s=1)
    axs[2, 1].plot(t_fit3, model_values3, 'g-', label='Fit')
    axs[2, 1].text(0.9, 0.95, f"Period = {period3:.8f} [day]\n Mode={snr3}", transform=axs[2, 1].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[2, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
    axs[2, 1].set_ylabel(f'$\Delta {lable_str}$ (mag)', fontsize=6, color='k')
    axs[2, 1].xaxis.set_minor_locator(MultipleLocator(0.25))  
    axs[2, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[2, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[2, 1].tick_params(axis='both', labelsize=7)
    axs[2, 1].invert_yaxis()
    
    fileName = f"ra={ra},dec={dec}.png"
    savepath3 = '/Users/qijia/Downloads/dmdsdr20/r/fig_test/3f/'
    fullPath = os.path.join(savepath3, fileName)
    plt.savefig(fullPath, format='png', dpi=300)
    
    plt.close() 



def plot_fourth(source,ra, dec,
            f1, p1, period1, snr1, f1_final, p1_max, phase1, each_star, t_fit, model_values,
            f2, p2, period2, snr2, f2_final, p2_max, phase2, t_fit2, model_values2, residual_mag,
            f3, p3, period3, snr3, f3_final, p3_max, phase3, t_fit3, model_values3, residual_mag2,
            f4, p4, period4, snr4, f4_final, p4_max, phase4, t_fit4, model_values4, residual_mag3,lable_str):
    
    
    fig, axs = plt.subplots(4, 2, figsize=(10, 12), dpi=300)
    axs[0, 0].scatter(f1_final, p1_max, marker='o', color='r', s=20, alpha=1)
    axs[0, 0].plot(f1, p1, color='b', linestyle='-', linewidth=1.0)
    axs[0, 0].text(0.9, 0.95, f"ZTF {source}", transform=axs[0, 0].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[0, 0].set_xlabel('Frequency', fontsize=6, color='k')
    axs[0, 0].set_ylabel('PSD', fontsize=6, color='k')
    axs[0, 0].xaxis.set_minor_locator(MultipleLocator(5))  
    axs[0, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[0, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[0, 0].tick_params(axis='both', labelsize=7)
    axs[0, 0].set_xlim(0,40) 
    axs[0, 0].set_ylim(0, None) 


    axs[0, 1].scatter(phase1, each_star.mag, color='r',s=1,alpha=0.7)
    axs[0, 1].scatter([p+1 for p in phase1], each_star.mag, color='r',s=1,alpha=0.7) 
    axs[0, 1].plot(t_fit, model_values, 'g-', alpha=1, label='Fit', linewidth=2, zorder=2) 
    axs[0, 1].text(0.9, 0.95, f"Period = {period1:.8f} [day]\n Mode={snr1}", transform=axs[0, 1].transAxes, fontsize=8,  fontweight='normal', va='top', ha='right', color='k')
    axs[0, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
    axs[0, 1].set_ylabel(f'${lable_str}$ (mag)', fontsize=6, color='k')
    axs[0, 1].xaxis.set_minor_locator(MultipleLocator(0.25))  
    axs[0, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[0, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[0, 1].tick_params(axis='both', labelsize=7)
    axs[0, 1].set_ylim(min(each_star.mag)-0.15,None) 
    axs[0, 1].invert_yaxis()



    axs[1, 0].scatter(f2_final, p2_max, marker='o', color='r', s=20, alpha=1)
    axs[1, 0].plot(f2, p2, color='b', linestyle='-', linewidth=1.0)    
    axs[1, 0].text(0.9, 0.95, f"Max_psd={p2_max}", transform=axs[1, 0].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[1, 0].set_xlabel('Frequency', fontsize=6, color='k')
    axs[1, 0].set_ylabel('PSD', fontsize=6, color='k')
    axs[1, 0].xaxis.set_minor_locator(MultipleLocator(5))  
    axs[1, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
    axs[1, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
    axs[1, 0].tick_params(axis='both', labelsize=7)
    axs[1, 0].set_xlim(0, 40) 
    axs[1, 0].set_ylim(0, None) 

    axs[1, 1].scatter(phase2, residual_mag, c='r', s=1)
    axs[1, 1].scatter([p+1 for p in phase2], residual_mag, c='r', s=1)
    axs[1 ,1].plot(t_fit2, model_values2, 'g-', alpha=1, label='Fit', linewidth=2, zorder=2) # 增加拟合线的线宽度
    axs[1, 1].text(0.9, 0.95, f"Period = {period2:.8f} [day]\n Mode={snr2}", transform=axs[1, 1].transAxes, fontsize=8,fontweight='normal', va='top', ha='right', color='k')
    axs[1, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
    axs[1, 1].set_ylabel(f'$\Delta {lable_str}$ (mag)', fontsize=6, color='k')
    axs[1, 1].xaxis.set_minor_locator(MultipleLocator(5))  
    axs[1, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
    axs[1, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k', grid_color='r', grid_alpha=0.5)
    axs[1, 1].tick_params(axis='both', labelsize=7)
    axs[1, 1].invert_yaxis()
    

    axs[2, 0].scatter(f3_final, p3_max, marker='o', color='r', s=20, alpha=1)
    axs[2, 0].plot(f3, p3, color='b', linestyle='-', linewidth=1.0)    
    axs[2, 0].text(0.9, 0.95, f"\nMax_psd={p3_max}", transform=axs[2, 0].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[2, 0].set_xlabel('Frequency', fontsize=6, color='k')
    axs[2, 0].set_ylabel('PSD', fontsize=6, color='k')
    axs[2, 0].xaxis.set_minor_locator(MultipleLocator(0.25))  
    axs[2, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[2, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[2, 0].tick_params(axis='both', labelsize=7)
    axs[2, 0].set_xlim(0,40) 
    axs[2, 0].set_ylim(0,None) 

    axs[2, 1].scatter(phase3, residual_mag2, c='r', s=1)
    axs[2, 1].scatter([p+1 for p in phase3], residual_mag2, c='r', s=1)
    axs[2, 1].plot(t_fit3, model_values3, 'g-', label='Fit')
    axs[2, 1].text(0.9, 0.95, f"Period = {period3:.8f} [day]\n Mode={snr3}", transform=axs[2, 1].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[2, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
    axs[2, 1].set_ylabel(f'$\Delta {lable_str}$ (mag)', fontsize=6, color='k')
    axs[2, 1].xaxis.set_minor_locator(MultipleLocator(0.25))  
    axs[2, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[2, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[2, 1].tick_params(axis='both', labelsize=7)
    axs[2, 1].invert_yaxis()


    axs[3, 0].scatter(f4_final, p4_max, marker='o', color='r', s=20, alpha=1)
    axs[3, 0].plot(f4, p4, color='b', linestyle='-', linewidth=1.0)    
    axs[3, 0].text(0.9, 0.95, f"\nMax_psd={p4_max}\n fap={fap4:.15f}", transform=axs[3, 0].transAxes, fontsize=8, fontweight='normal', va='top', ha='right', color='k')
    axs[3, 0].set_xlabel('Frequency', fontsize=6, color='k')
    axs[3, 0].set_ylabel('PSD', fontsize=6, color='k')
    axs[3, 0].xaxis.set_minor_locator(MultipleLocator(5))  
    axs[3, 0].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[3, 0].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[3, 0].tick_params(axis='both', labelsize=7)
    axs[3, 0].set_xlim(0,40) 
    axs[3, 0].set_ylim(0,None) 

    axs[3, 1].scatter(phase3, residual_mag3, c='r', s=1)
    axs[3, 1].scatter([p+1 for p in phase4], residual_mag3, c='r', s=1)
    axs[3 ,1].plot(t_fit4, model_values4, 'g-', alpha=1, label='Fit', linewidth=2, zorder=2) 
    axs[3, 1].text(0.9, 0.95, f"Period = {period4:.8f} [day]\n{snr4}", transform=axs[3, 1].transAxes, fontsize=8,  fontweight='normal', va='top', ha='right', color='k')
    axs[3, 1].set_xlabel('Pulsation phase', fontsize=6, color='k')
    axs[3, 1].set_ylabel(f'$\Delta {lable_str}$ (mag)', fontsize=6, color='k')
    axs[3, 1].xaxis.set_minor_locator(MultipleLocator(0.25))  
    axs[3, 1].tick_params(axis='both', which='major', direction='in', length=4, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[3, 1].tick_params(axis='both', which='minor', direction='in', length=2, width=0.8, colors='k',grid_color='r', grid_alpha=0.5)
    axs[3, 1].tick_params(axis='both', labelsize=7)
    axs[3, 1].invert_yaxis()

    savepath4 = '/Users/qijia/Downloads/dmdsdr20/r/fig_test/4f/'
    fileName = f"ra={ra},dec={dec}.png"
    fullPath = os.path.join(savepath4, fileName)
    plt.savefig(fullPath, format='png', dpi=300)
    plt.close() 

