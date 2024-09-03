import double_modediscern as fm2f

def triplemodediscern(period1,period2,period3):
    
    
    if period1>period2>period3:
        ratio1=period2/period1
        ratio2=period3/period2
        ratio3=period3/period1

        if 0.88>ratio2>ratio1>ratio3>0.46 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.66>ratio3>0.59:
            ##2O/1O/F
            period1_Mode='F'
            period2_Mode='1O'
            period3_Mode='2O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.59<ratio1<0.66 and 0.88>ratio2>0.82 and 0.46<ratio3<0.58 :
            ##3O/2O/F
            period1_Mode='F'
            period2_Mode='2O'
            period3_Mode='3O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.76<ratio1<0.86 and 0.80<ratio2<0.88 and 0.63<ratio3<0.72:
            ##3O/2O/1O
            period1_Mode='1O'
            period2_Mode='2O'
            period3_Mode='3O'

        elif 0.88>ratio1>ratio2>ratio3>0.46 and 0.74<ratio1<0.82 and 0.63<ratio2<0.72 and 0.46<ratio3<0.58:
            ##3O/1O/F
            period1_Mode='F'
            period2_Mode='1O'
            period3_Mode='3O'


        else:
            period1_ms,period2_ms=fm2f.doubleModediscern(period1,period2)
            dou_count1=0
            if period1_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1
            if period2_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1
            
            period1_sds,period3_sds=fm2f.doubleModediscern(period1,period3)
            dou_count2=0
            if period1_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1
            if period3_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1

            period2_jsj,period3_jsj=fm2f.doubleModediscern(period2,period3)
            dou_count3=0
            if period2_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1
            if period3_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1


            if dou_count1>dou_count2 and dou_count1>dou_count3:
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            elif dou_count2>dou_count1 and dou_count2>dou_count3:
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0
            elif dou_count3>dou_count1 and dou_count3>dou_count2:
                period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)
                period1_Mode=0
            elif (dou_count1==dou_count2 and dou_count1>dou_count3) or (dou_count1==dou_count3 and dou_count1>dou_count2):
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            else:
                # dou_count2==dou_count3 and dou_count2>dou_count1
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0





    elif period1>period3>period2:
        ratio1=period3/period1
        ratio2=period2/period3
        ratio3=period2/period1

        if 0.88>ratio2>ratio1>ratio3>0.46 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.66>ratio3>0.59:
            ##2O/1O/F
            period1_Mode='F'
            period3_Mode='1O'
            period2_Mode='2O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.59<ratio1<0.66 and 0.88>ratio2>0.82 and 0.46<ratio3<0.58 :
            ##3O/2O/F
            period1_Mode='F'
            period3_Mode='2O'
            period2_Mode='3O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.76<ratio1<0.86 and 0.80<ratio2<0.88 and 0.63<ratio3<0.72:
            ##3O/2O/1O
            period1_Mode='1O'
            period3_Mode='2O'
            period2_Mode='3O'

        elif 0.88>ratio1>ratio2>ratio3>0.46 and 0.74<ratio1<0.82 and 0.63<ratio2<0.72 and 0.46<ratio3<0.58:
            ##3O/1O/F
            period1_Mode='F'
            period3_Mode='1O'
            period2_Mode='3O'


        else:
            period1_ms,period2_ms=fm2f.doubleModediscern(period1,period2)
            dou_count1=0
            if period1_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1
            if period2_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1

            
            period1_sds,period3_sds=fm2f.doubleModediscern(period1,period3)
            dou_count2=0
            if period1_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1
            if period3_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1

            period2_jsj,period3_jsj=fm2f.doubleModediscern(period2,period3)
            dou_count3=0
            if period2_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1
            if period3_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1



            if dou_count1>dou_count2 and dou_count1>dou_count3:
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            elif dou_count2>dou_count1 and dou_count2>dou_count3:
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0
            elif dou_count3>dou_count1 and dou_count3>dou_count2:
                period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)
                period1_Mode=0
            elif (dou_count1==dou_count2 and dou_count1>dou_count3) or (dou_count1==dou_count3 and dou_count1>dou_count2):
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            else:
                # dou_count2==dou_count3 and dou_count2>dou_count1
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0


    elif period2>period1>period3:
        ratio1=period1/period2
        ratio2=period3/period1
        ratio3=period3/period2

        if 0.88>ratio2>ratio1>ratio3>0.46 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.66>ratio3>0.59:
            ##2O/1O/F
            period2_Mode='F'
            period1_Mode='1O'
            period3_Mode='2O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.59<ratio1<0.66 and 0.88>ratio2>0.82 and 0.46<ratio3<0.58 :
            ##3O/2O/F
            period2_Mode='F'
            period1_Mode='2O'
            period3_Mode='3O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.76<ratio1<0.86 and 0.80<ratio2<0.88 and 0.63<ratio3<0.72:
            ##3O/2O/1O
            period2_Mode='1O'
            period1_Mode='2O'
            period3_Mode='3O'

        elif 0.88>ratio1>ratio2>ratio3>0.46 and 0.74<ratio1<0.82 and 0.63<ratio2<0.72 and 0.46<ratio3<0.58:
            ##3O/1O/F
            period2_Mode='F'
            period1_Mode='1O'
            period3_Mode='3O'



        else:
            period1_ms,period2_ms=fm2f.doubleModediscern(period1,period2)
            dou_count1=0
            if period1_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1
            if period2_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1

            
            period1_sds,period3_sds=fm2f.doubleModediscern(period1,period3)
            dou_count2=0
            if period1_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1
            if period3_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1

            period2_jsj,period3_jsj=fm2f.doubleModediscern(period2,period3)
            dou_count3=0
            if period2_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1
            if period3_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1



            if dou_count1>dou_count2 and dou_count1>dou_count3:
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            elif dou_count2>dou_count1 and dou_count2>dou_count3:
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0
            elif dou_count3>dou_count1 and dou_count3>dou_count2:
                period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)
                period1_Mode=0
            elif (dou_count1==dou_count2 and dou_count1>dou_count3) or (dou_count1==dou_count3 and dou_count1>dou_count2):
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            else:
                # dou_count2==dou_count3 and dou_count2>dou_count1
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0


##231
    elif period2>period3>period1:
        ratio1=period3/period2
        ratio2=period1/period3
        ratio3=period1/period2

        if 0.88>ratio2>ratio1>ratio3>0.46 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.66>ratio3>0.59:
            ##2O/1O/F
            period2_Mode='F'
            period3_Mode='1O'
            period1_Mode='2O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.59<ratio1<0.66 and 0.88>ratio2>0.82 and 0.46<ratio3<0.58 :
            ##3O/2O/F
            period2_Mode='F'
            period3_Mode='2O'
            period1_Mode='3O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.76<ratio1<0.86 and 0.80<ratio2<0.88 and 0.63<ratio3<0.72:
            ##3O/2O/1O
            period2_Mode='1O'
            period3_Mode='2O'
            period1_Mode='3O'

        elif 0.88>ratio1>ratio2>ratio3>0.46 and 0.74<ratio1<0.82 and 0.63<ratio2<0.72 and 0.46<ratio3<0.58:
            ##3O/1O/F
            period2_Mode='F'
            period3_Mode='1O'
            period1_Mode='3O'


        else:
            period1_ms,period2_ms=fm2f.doubleModediscern(period1,period2)
            dou_count1=0
            if period1_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1
            if period2_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1

            
            period1_sds,period3_sds=fm2f.doubleModediscern(period1,period3)
            dou_count2=0
            if period1_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1
            if period3_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1

            period2_jsj,period3_jsj=fm2f.doubleModediscern(period2,period3)
            dou_count3=0
            if period2_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1
            if period3_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1



            if dou_count1>dou_count2 and dou_count1>dou_count3:
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            elif dou_count2>dou_count1 and dou_count2>dou_count3:
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0
            elif dou_count3>dou_count1 and dou_count3>dou_count2:
                period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)
                period1_Mode=0
            elif (dou_count1==dou_count2 and dou_count1>dou_count3) or (dou_count1==dou_count3 and dou_count1>dou_count2):
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            else:
                # dou_count2==dou_count3 and dou_count2>dou_count1
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0

##312
    elif period3>period1>period2:
        ratio1=period1/period3
        ratio2=period2/period1
        ratio3=period2/period3

        if 0.88>ratio2>ratio1>ratio3>0.46 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.66>ratio3>0.59:
            ##2O/1O/F
            period3_Mode='F'
            period1_Mode='1O'
            period2_Mode='2O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.59<ratio1<0.66 and 0.88>ratio2>0.82 and 0.46<ratio3<0.58 :
            ##3O/2O/F
            period3_Mode='F'
            period1_Mode='2O'
            period2_Mode='3O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.76<ratio1<0.86 and 0.80<ratio2<0.88 and 0.63<ratio3<0.72:
            ##3O/2O/1O
            period3_Mode='1O'
            period1_Mode='2O'
            period2_Mode='3O'

        elif 0.88>ratio1>ratio2>ratio3>0.46 and 0.74<ratio1<0.82 and 0.63<ratio2<0.72 and 0.46<ratio3<0.58:
            ##3O/1O/F
            period3_Mode='F'
            period1_Mode='1O'
            period2_Mode='3O'




        else:
            period1_ms,period2_ms=fm2f.doubleModediscern(period1,period2)
            dou_count1=0
            if period1_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1
            if period2_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1

            
            period1_sds,period3_sds=fm2f.doubleModediscern(period1,period3)
            dou_count2=0
            if period1_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1
            if period3_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1

            period2_jsj,period3_jsj=fm2f.doubleModediscern(period2,period3)
            dou_count3=0
            if period2_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1
            if period3_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1



            if dou_count1>dou_count2 and dou_count1>dou_count3:
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            elif dou_count2>dou_count1 and dou_count2>dou_count3:
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0
            elif dou_count3>dou_count1 and dou_count3>dou_count2:
                period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)
                period1_Mode=0
            elif (dou_count1==dou_count2 and dou_count1>dou_count3) or (dou_count1==dou_count3 and dou_count1>dou_count2):
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            else:
                # dou_count2==dou_count3 and dou_count2>dou_count1
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0

##321
    else:
        ratio1=period2/period3
        ratio2=period1/period2
        ratio3=period1/period3

        if 0.88>ratio2>ratio1>ratio3>0.46 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.66>ratio3>0.59:
            ##2O/1O/F
            period3_Mode='F'
            period2_Mode='1O'
            period1_Mode='2O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.59<ratio1<0.66 and 0.88>ratio2>0.82 and 0.46<ratio3<0.58 :
            ##3O/2O/F
            period3_Mode='F'
            period2_Mode='2O'
            period1_Mode='3O'

        elif 0.88>ratio2>ratio1>ratio3>0.46 and 0.76<ratio1<0.86 and 0.80<ratio2<0.88 and 0.63<ratio3<0.72:
            ##3O/2O/1O
            period3_Mode='1O'
            period2_Mode='2O'
            period1_Mode='3O'

        elif 0.88>ratio1>ratio2>ratio3>0.46 and 0.74<ratio1<0.82 and 0.63<ratio2<0.72 and 0.46<ratio3<0.58:
            ##3O/1O/F
            period3_Mode='F'
            period2_Mode='1O'
            period1_Mode='3O'


        else:
            period1_ms,period2_ms=fm2f.doubleModediscern(period1,period2)
            dou_count1=0
            if period1_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1
            if period2_ms in ['F', '1O', '2O', '3O']:
                dou_count1 +=1

            
            period1_sds,period3_sds=fm2f.doubleModediscern(period1,period3)
            dou_count2=0
            if period1_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1
            if period3_sds in ['F', '1O', '2O', '3O']:
                dou_count2 +=1

            period2_jsj,period3_jsj=fm2f.doubleModediscern(period2,period3)
            dou_count3=0
            if period2_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1
            if period3_jsj in ['F', '1O', '2O', '3O']:
                dou_count3 +=1



            if dou_count1>dou_count2 and dou_count1>dou_count3:
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            elif dou_count2>dou_count1 and dou_count2>dou_count3:
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0
            elif dou_count3>dou_count1 and dou_count3>dou_count2:
                period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)
                period1_Mode=0
            elif (dou_count1==dou_count2 and dou_count1>dou_count3) or (dou_count1==dou_count3 and dou_count1>dou_count2):
                period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)
                period3_Mode=0
            else:
                # dou_count2==dou_count3 and dou_count2>dou_count1
                period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)
                period2_Mode=0


    return period1_Mode,period2_Mode,period3_Mode