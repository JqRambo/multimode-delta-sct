import fivethmodediscern as fm5f
import fourthmodediscern as fm4f
import triplemodediscern as fm3f
import double_modediscern as fm2f

def sixthmodediscern(period1,period2,period3,period4,period5,period6,period1_mode,period2_mode,period3_mode,period4_mode,period5_mode,period6_mode):
    
    if period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==1 and period6_mode==1:

        period1_bn,period2_bn,period3_bn,period4_bn,period5_bn=fm5f.fivethmodediscern(period1,period2,period3,period4,period5,period1_mode,period2_mode,period3_mode,period4_mode,period5_mode)
        sixsd_count1=0

        if period1_bn in ['F', '1O', '2O', '3O']:
            sixsd_count1 += 1
        if period2_bn in ['F', '1O', '2O', '3O']:
            sixsd_count1 +=1
        if period3_bn in ['F', '1O', '2O', '3O']:
            sixsd_count1 +=1 
        if period4_bn in ['F', '1O', '2O', '3O']:
            sixsd_count1 +=1
        if period5_bn in ['F', '1O', '2O', '3O']:
            sixsd_count1 +=1

        period1_bq,period2_bq,period3_bq,period4_bq,period6_bq=fm5f.fivethmodediscern(period1,period2,period3,period4,period6,period1_mode,period2_mode,period3_mode,period4_mode,period6_mode)
        sixsd_count2=0

        if period1_bq in ['F', '1O', '2O', '3O']:
            sixsd_count2 += 1
        if period2_bq in ['F', '1O', '2O', '3O']:
            sixsd_count2 +=1
        if period3_bq in ['F', '1O', '2O', '3O']:
            sixsd_count2 +=1 
        if period4_bq in ['F', '1O', '2O', '3O']:
            sixsd_count2 +=1
        if period6_bq in ['F', '1O', '2O', '3O']:
            sixsd_count2 +=1


        period1_bz,period2_bz,period3_bz,period5_bz,period6_bz=fm5f.fivethmodediscern(period1,period2,period3,period5,period6,period1_mode,period2_mode,period3_mode,period5_mode,period6_mode)
        sixsd_count3=0

        if period1_bz in ['F', '1O', '2O', '3O']:
            sixsd_count3 += 1
        if period2_bz in ['F', '1O', '2O', '3O']:
            sixsd_count3 +=1
        if period3_bz in ['F', '1O', '2O', '3O']:
            sixsd_count3 +=1 
        if period5_bz in ['F', '1O', '2O', '3O']:
            sixsd_count3 +=1
        if period6_bz in ['F', '1O', '2O', '3O']:
            sixsd_count3 +=1


        period1_br,period2_br,period4_br,period5_br,period6_br=fm5f.fivethmodediscern(period1,period2,period4,period5,period6,period1_mode,period2_mode,period4_mode,period5_mode,period6_mode)
        sixsd_count4=0

        if period1_br in ['F', '1O', '2O', '3O']:
            sixsd_count4 += 1
        if period2_br in ['F', '1O', '2O', '3O']:
            sixsd_count4 +=1
        if period4_br in ['F', '1O', '2O', '3O']:
            sixsd_count4 +=1 
        if period5_br in ['F', '1O', '2O', '3O']:
            sixsd_count4 +=1
        if period6_br in ['F', '1O', '2O', '3O']:
            sixsd_count4 +=1


        period1_qr,period3_qr,period4_qr,period5_qr,period6_qr=fm5f.fivethmodediscern(period1,period3,period4,period5,period6,period1_mode,period3_mode,period4_mode,period5_mode,period6_mode)
        sixsd_count5=0

        if period1_qr in ['F', '1O', '2O', '3O']:
            sixsd_count5 += 1
        if period3_qr in ['F', '1O', '2O', '3O']:
            sixsd_count5 +=1
        if period4_qr in ['F', '1O', '2O', '3O']:
            sixsd_count5 +=1 
        if period5_qr in ['F', '1O', '2O', '3O']:
            sixsd_count5 +=1
        if period6_qr in ['F', '1O', '2O', '3O']:
            sixsd_count5 +=1



        period2_wr,period3_wr,period4_wr,period5_wr,period6_wr=fm5f.fivethmodediscern(period2,period3,period4,period5,period6,period2_mode,period3_mode,period4_mode,period5_mode,period6_mode)
        sixsd_count6=0

        if period2_wr in ['F', '1O', '2O', '3O']:
            sixsd_count6 += 1
        if period3_wr in ['F', '1O', '2O', '3O']:
            sixsd_count6 +=1
        if period4_wr in ['F', '1O', '2O', '3O']:
            sixsd_count6 +=1 
        if period5_wr in ['F', '1O', '2O', '3O']:
            sixsd_count6 +=1
        if period6_wr in ['F', '1O', '2O', '3O']:
            sixsd_count6 +=1



        if max(sixsd_count1, sixsd_count2, sixsd_count3, sixsd_count4,sixsd_count5,sixsd_count6)==sixsd_count1:
            period1_Mode,period2_Mode,period3_Mode,period4_Mode,period5_Mode=fm5f.fivethmodediscern(period1,period2,period3,period4,period5,period1_mode,period2_mode,period3_mode,period4_mode,period5_mode)
            period6_Mode=0
        elif max(sixsd_count1, sixsd_count2, sixsd_count3, sixsd_count4,sixsd_count5,sixsd_count6)==sixsd_count2:
            period1_Mode,period2_Mode,period3_Mode,period4_Mode,period6_Mode=fm5f.fivethmodediscern(period1,period2,period3,period4,period6,period1_mode,period2_mode,period3_mode,period4_mode,period6_mode)
            period5_Mode=0
        elif max(sixsd_count1, sixsd_count2, sixsd_count3, sixsd_count4,sixsd_count5,sixsd_count6)==sixsd_count3:
            period1_Mode,period2_Mode,period3_Mode,period5_Mode,period6_Mode=fm5f.fivethmodediscern(period1,period2,period3,period5,period6,period1_mode,period2_mode,period3_mode,period5_mode,period6_mode)
            period4_Mode=0
        elif max(sixsd_count1, sixsd_count2, sixsd_count3, sixsd_count4,sixsd_count5,sixsd_count6)==sixsd_count4:
            period1_Mode,period2_Mode,period4_Mode,period5_Mode,period6_Mode=fm5f.fivethmodediscern(period1,period2,period4,period5,period6,period1_mode,period2_mode,period4_mode,period5_mode,period6_mode)
            period3_Mode=0
        elif max(sixsd_count1, sixsd_count2, sixsd_count3, sixsd_count4,sixsd_count5,sixsd_count6)==sixsd_count5:
            period1_Mode,period3_Mode,period4_Mode,period5_Mode,period6_Mode=fm5f.fivethmodediscern(period1,period3,period4,period5,period6,period1_mode,period3_mode,period4_mode,period5_mode,period6_mode)
            period2_Mode=0
        else:
            period2_Mode,period3_Mode,period4_Mode,period5_Mode,period6_Mode=fm5f.fivethmodediscern(period2,period3,period4,period5,period6,period2_mode,period3_mode,period4_mode,period5_mode,period6_mode)
            period1_Mode=0



    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==1 and period6_mode==0:
        period1_Mode,period2_Mode,period3_Mode,period4_Mode,period5_Mode=fm5f.fivethmodediscern(period1,period2,period3,period4,period5,period1_mode,period2_mode,period3_mode,period4_mode,period5_mode)
        period6_Mode=0
    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==0 and period6_mode==1:
        period1_Mode,period2_Mode,period3_Mode,period4_Mode,period6_Mode=fm5f.fivethmodediscern(period1,period2,period3,period4,period6,period1_mode,period2_mode,period3_mode,period4_mode,period6_mode)
        period5_Mode=0
    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==1 and period6_mode==1:
        period1_Mode,period2_Mode,period3_Mode,period5_Mode,period6_Mode=fm5f.fivethmodediscern(period1,period2,period3,period5,period6,period1_mode,period2_mode,period3_mode,period5_mode,period6_mode)
        period4_Mode=0
    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==1 and period6_mode==1:
        period1_Mode,period2_Mode,period4_Mode,period5_Mode,period6_Mode=fm5f.fivethmodediscern(period1,period2,period4,period5,period6,period1_mode,period2_mode,period4_mode,period5_mode,period6_mode)
        period3_Mode=0
    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==1 and period6_mode==1:
        period1_Mode,period3_Mode,period4_Mode,period5_Mode,period6_Mode=fm5f.fivethmodediscern(period1,period3,period4,period5,period6,period1_mode,period3_mode,period4_mode,period5_mode,period6_mode)
        period2_Mode=0
    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==1 and period6_mode==1:
        period2_Mode,period3_Mode,period4_Mode,period5_Mode,period6_Mode=fm5f.fivethmodediscern(period2,period3,period4,period5,period6,period2_mode,period3_mode,period4_mode,period5_mode,period6_mode)
        period1_Mode=0

##
    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==0 and period6_mode==0:

        period1_Mode,period2_Mode,period3_Mode,period4_Mode=fm4f.fourthmodediscern(period1,period2,period3,period4,period1_mode,period2_mode,period3_mode,period4_mode)
        period5_Mode=0
        period6_Mode=0

    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==1 and period6_mode==0:
        
        period1_Mode,period2_Mode,period3_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period3,period5,period1_mode,period2_mode,period3_mode,period5_mode)
        period4_Mode=0
        period6_Mode=0

    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==0 and period6_mode==1:
        
        period1_Mode,period2_Mode,period3_Mode,period6_Mode=fm4f.fourthmodediscern(period1,period2,period3,period6,period1_mode,period2_mode,period3_mode,period6_mode)
        period4_Mode=0
        period5_Mode=0


    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==1 and period6_mode==0:
        
        period1_Mode,period2_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period4,period5,period1_mode,period2_mode,period4_mode,period5_mode)
        period3_Mode=0
        period6_Mode=0

    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0 and period6_mode==1:
        
        period1_Mode,period2_Mode,period4_Mode,period6_Mode=fm4f.fourthmodediscern(period1,period2,period4,period6,period1_mode,period2_mode,period4_mode,period6_mode)
        period3_Mode=0
        period5_Mode=0


    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==1 and period6_mode==1:
        
        period1_Mode,period2_Mode,period5_Mode,period6_Mode=fm4f.fourthmodediscern(period1,period2,period5,period6,period1_mode,period2_mode,period5_mode,period6_mode)
        period3_Mode=0
        period4_Mode=0
##
    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==1 and period6_mode==0:
        period2_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period2,period3,period4,period5,period2_mode,period3_mode,period4_mode,period5_mode)
        period1_Mode=0
        period6_Mode=0

    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==0 and period6_mode==1:
        period2_Mode,period3_Mode,period4_Mode,period6_Mode=fm4f.fourthmodediscern(period2,period3,period4,period6,period2_mode,period3_mode,period4_mode,period6_mode)
        period1_Mode=0
        period5_Mode=0


    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==1 and period6_mode==1:
        period3_Mode,period4_Mode,period5_Mode,period6_Mode=fm4f.fourthmodediscern(period3,period4,period5,period6,period3_mode,period4_mode,period5_mode,period6_mode)
        period1_Mode=0
        period2_Mode=0

##
    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==0 and period6_mode==0:
        period4_Mode=0
        period5_Mode=0
        period6_Mode=0
        period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)


    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0 and period6_mode==0:
        period3_Mode=0
        period5_Mode=0
        period6_Mode=0
        period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)


    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==1 and period6_mode==0:
        period3_Mode=0
        period4_Mode=0
        period6_Mode=0
        period1_Mode,period2_Mode,period5_Mode=fm3f.triplemodediscern(period1,period2,period5)

    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==0 and period6_mode==1:
        period3_Mode=0
        period4_Mode=0
        period5_Mode=0
        period1_Mode,period2_Mode,period6_Mode=fm3f.triplemodediscern(period1,period2,period6)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==0 and period6_mode==0:
        period2_Mode=0
        period5_Mode=0
        period6_Mode=0
        period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==1 and period6_mode==0:
        period2_Mode=0
        period4_Mode=0
        period6_Mode=0
        period1_Mode,period3_Mode,period5_Mode=fm3f.triplemodediscern(period1,period3,period5)

    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==0 and period6_mode==1:
        period2_Mode=0
        period4_Mode=0
        period5_Mode=0
        period1_Mode,period3_Mode,period6_Mode=fm3f.triplemodediscern(period1,period3,period6)


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==1 and period6_mode==0:
        period2_Mode=0
        period3_Mode=0
        period6_Mode=0
        period1_Mode,period4_Mode,period5_Mode=fm3f.triplemodediscern(period1,period4,period5)


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==0 and period6_mode==1:
        period2_Mode=0
        period3_Mode=0
        period5_Mode=0
        period1_Mode,period4_Mode,period6_Mode=fm3f.triplemodediscern(period1,period4,period6)


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==0 and period5_mode==1 and period6_mode==1:
        period2_Mode=0
        period3_Mode=0
        period4_Mode=0
        period1_Mode,period5_Mode,period6_Mode=fm3f.triplemodediscern(period1,period5,period6)


##

    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==0 and period6_mode==0:
        period1_Mode=0
        period5_Mode=0
        period6_Mode=0
        period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)


    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==1 and period6_mode==0:
        period1_Mode=0
        period4_Mode=0
        period6_Mode=0
        period2_Mode,period3_Mode,period5_Mode=fm3f.triplemodediscern(period2,period3,period5)

    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==0 and period6_mode==1:
        period1_Mode=0
        period4_Mode=0
        period5_Mode=0
        period2_Mode,period3_Mode,period6_Mode=fm3f.triplemodediscern(period2,period3,period6)


    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==1 and period6_mode==0:
        period1_Mode=0
        period3_Mode=0
        period6_Mode=0
        period2_Mode,period4_Mode,period5_Mode=fm3f.triplemodediscern(period2,period4,period5)



    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0 and period6_mode==1:
        period1_Mode=0
        period3_Mode=0
        period5_Mode=0
        period2_Mode,period4_Mode,period6_Mode=fm3f.triplemodediscern(period2,period4,period5)

    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==1 and period6_mode==1:
        period1_Mode=0
        period3_Mode=0
        period4_Mode=0
        period2_Mode,period5_Mode,period6_Mode=fm3f.triplemodediscern(period2,period5,period6)


##
    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==1 and period6_mode==0:
        period1_Mode=0
        period2_Mode=0
        period6_Mode=0
        period3_Mode,period4_Mode,period5_Mode=fm3f.triplemodediscern(period3,period4,period5)


    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==0 and period6_mode==1:
        period1_Mode=0
        period2_Mode=0
        period5_Mode=0
        period3_Mode,period4_Mode,period6_Mode=fm3f.triplemodediscern(period3,period4,period6)

    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==1 and period6_mode==1:
        period1_Mode=0
        period2_Mode=0
        period3_Mode=0
        period4_Mode,period5_Mode,period6_Mode=fm3f.triplemodediscern(period4,period5,period6)


##
    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==0 and period6_mode==0:
        period3_Mode=0
        period4_Mode=0
        period5_Mode=0
        period6_Mode=0
        period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==0 and period6_mode==0:
        period2_Mode=0
        period4_Mode=0
        period5_Mode=0
        period6_Mode=0
        period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)

        
    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==0 and period6_mode==0:
        period2_Mode=0
        period3_Mode=0
        period5_Mode=0
        period6_Mode=0
        period1_Mode,period4_Mode=fm2f.doubleModediscern(period1,period4)



    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==0 and period5_mode==1 and period6_mode==0:
        period2_Mode=0
        period3_Mode=0
        period4_Mode=0
        period6_Mode=0
        period1_Mode,period5_Mode=fm2f.doubleModediscern(period1,period5)

    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==0 and period5_mode==0 and period6_mode==1:
        period2_Mode=0
        period3_Mode=0
        period4_Mode=0
        period5_Mode=0
        period1_Mode,period6_Mode=fm2f.doubleModediscern(period1,period6)


##
    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==0 and period6_mode==0:
        period1_Mode=0
        period4_Mode=0
        period5_Mode=0
        period6_Mode=0
        period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)


    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0 and period6_mode==0:
        period1_Mode=0
        period3_Mode=0
        period5_Mode=0
        period6_Mode=0
        period2_Mode,period4_Mode=fm2f.doubleModediscern(period2,period4)
  
    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==1 and period6_mode==0:
        period1_Mode=0
        period3_Mode=0
        period4_Mode=0
        period6_Mode=0
        period2_Mode,period5_Mode=fm2f.doubleModediscern(period2,period5)
  

    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==0 and period6_mode==1:
        period1_Mode=0
        period3_Mode=0
        period4_Mode=0
        period5_Mode=0
        period2_Mode,period6_Mode=fm2f.doubleModediscern(period2,period6)
  

##
        
    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==0 and period6_mode==0:
        period1_Mode=0
        period2_Mode=0
        period5_Mode=0
        period6_Mode=0
        period3_Mode,period4_Mode=fm2f.doubleModediscern(period3,period4)
  
    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==1 and period6_mode==0:
        period1_Mode=0
        period2_Mode=0
        period4_Mode=0
        period6_Mode=0
        period3_Mode,period5_Mode=fm2f.doubleModediscern(period3,period5)
  
    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==0 and period6_mode==1:
        period1_Mode=0
        period2_Mode=0
        period4_Mode=0
        period5_Mode=0
        period3_Mode,period6_Mode=fm2f.doubleModediscern(period3,period6)
  

    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==1 and period6_mode==0:
        period1_Mode=0
        period2_Mode=0
        period3_Mode=0
        period6_Mode=0
        period4_Mode,period5_Mode=fm2f.doubleModediscern(period4,period5)
   

    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==0 and period6_mode==1:
        period1_Mode=0
        period2_Mode=0
        period3_Mode=0
        period5_Mode=0
        period4_Mode,period6_Mode=fm2f.doubleModediscern(period4,period6)
   
    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==0 and period5_mode==1 and period6_mode==1:
        period1_Mode=0
        period2_Mode=0
        period3_Mode=0
        period4_Mode=0
        period5_Mode,period6_Mode=fm2f.doubleModediscern(period5,period6)
   

    else:
        period1_Mode=0
        period2_Mode=0
        period3_Mode=0
        period4_Mode=0
        period5_Mode=0
        period6_Mode=0

    return period1_Mode,period2_Mode,period3_Mode,period4_Mode,period5_Mode,period6_Mode



