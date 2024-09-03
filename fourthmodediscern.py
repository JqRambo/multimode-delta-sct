import triplemodediscern as fm3f
import double_modediscern as fm2f

def fourthmodediscern(period1,period2,period3,period4,period1_mode,period2_mode,period3_mode,period4_mode):
    
    if period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1:
        if period1>period2>period3>period4:
            ratio1=period2/period1#
            ratio2=period3/period2

            ratio3=period4/period3

            ratio4=period3/period1

            ratio5=period4/period2
            ratio6=period4/period1

            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='F'
                period2_Mode='1O'
                period3_Mode='2O'
                period4_Mode='3O'



            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1

                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period2_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period2_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1



                # if dsdt_count1>dsdt_count2 and dsdt_count1>dsdt_count3 and dsdt_count1>dsdt_count4:
                #     period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                #     period4_Mode=0
                # elif dsdt_count2>dsdt_count1 and dsdt_count2>dsdt_count3 and dsdt_count2>dsdt_count4:
                #     period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                #     period3_Mode=0
                # elif dsdt_count3>dsdt_count1 and dsdt_count3>dsdt_count2 and dsdt_count3>dsdt_count4:
                #     period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                #     period2_Mode=0
                # elif dsdt_count4>dsdt_count1 and dsdt_count4>dsdt_count2 and dsdt_count4>dsdt_count3:
                #     period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                #     period1_Mode=0

                # elif (dsdt_count1>dsdt_count2 and dsdt_count1>dsdt_count3 and dsdt_count1>dsdt_count4) or (dsdt_count1==dsdt_count2 and dsdt_count1>dsdt_count3 and dsdt_count1>dsdt_count4) or (dsdt_count1==dsdt_count3 and dsdt_count1>dsdt_count2 and dsdt_count1>dsdt_count4) or (dsdt_count1==dsdt_count4 and dsdt_count1>dsdt_count2 and dsdt_count1>dsdt_count3) or (dsdt_count1==dsdt_count2==dsdt_count3 and dsdt_count1>dsdt_count4) or (dsdt_count1==dsdt_count2==dsdt_count4 and dsdt_count1>dsdt_count3) or (dsdt_count1==dsdt_count3==dsdt_count4 and dsdt_count1>dsdt_count2) or (dsdt_count2==dsdt_count3==dsdt_count4 and dsdt_count1>dsdt_count2) or (dsdt_count1==dsdt_count2==dsdt_count3==dsdt_count4):


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


        elif period1>period2>period4>period3:
            ratio1=period2/period1
            ratio2=period4/period2
            ratio3=period3/period4
            ratio4=period4/period1
            ratio5=period3/period2
            ratio6=period3/period1
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='F'
                period2_Mode='1O'
                period3_Mode='3O'
                period4_Mode='2O'

            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0



        elif period1>period3>period2>period4:
            ratio1=period3/period1
            ratio2=period2/period3
            ratio3=period4/period2
            ratio4=period2/period1
            ratio5=period4/period3
            ratio6=period4/period1
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='F'
                period2_Mode='2O'
                period3_Mode='1O'
                period4_Mode='3O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0

 
                            
        elif period1>period3>period4>period2:
            ratio1=period3/period1
            ratio2=period4/period3
            ratio3=period2/period4
            ratio4=period4/period1
            ratio5=period2/period3
            ratio6=period2/period1
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='F'
                period2_Mode='3O'
                period3_Mode='1O'
                period4_Mode='2O'
            
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1

                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0



        elif period1>period4>period2>period3:
            ratio1=period4/period1
            ratio2=period2/period4
            ratio3=period3/period2
            ratio4=period2/period1
            ratio5=period3/period4
            ratio6=period3/period1

            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='F'
                period2_Mode='2O'
                period3_Mode='3O'
                period4_Mode='1O'

            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


        elif period1>period4>period3>period2:
            ratio1=period4/period1
            ratio2=period3/period4
            ratio3=period2/period3
            ratio4=period3/period1
            ratio5=period2/period4
            ratio6=period2/period1
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='F'
                period2_Mode='3O'
                period3_Mode='2O'
                period4_Mode='1O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0

  

        elif period2>period1>period3>period4:
            ratio1=period1/period2
            ratio2=period3/period1
            ratio3=period4/period3
            ratio4=period3/period2
            ratio5=period4/period1
            ratio6=period4/period2
            
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='1O'
                period2_Mode='F'
                period3_Mode='2O'
                period4_Mode='3O'


            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


        elif period2>period1>period4>period3:
            ratio1=period1/period2
            ratio2=period4/period1
            ratio3=period3/period4
            ratio4=period4/period2
            ratio5=period3/period1
            ratio6=period3/period2
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='1O'
                period2_Mode='F'
                period3_Mode='3O'
                period4_Mode='2O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


        elif period2>period3>period1>period4:
            ratio1=period3/period2
            ratio2=period1/period3
            ratio3=period4/period1
            ratio4=period1/period2
            ratio5=period4/period3
            ratio6=period4/period2
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='2O'
                period2_Mode='F'
                period3_Mode='1O'
                period4_Mode='3O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1

                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0

 

        elif period2>period3>period4>period1:
            ratio1=period3/period2
            ratio2=period4/period3
            ratio3=period1/period4
            ratio4=period4/period2
            ratio5=period1/period3
            ratio6=period1/period2
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='3O'
                period2_Mode='F'
                period3_Mode='1O'
                period4_Mode='2O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


        elif period2>period4>period1>period3:
            ratio1=period4/period2
            ratio2=period1/period4
            ratio3=period3/period1
            ratio4=period1/period2
            ratio5=period3/period4
            ratio6=period3/period2
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='2O'
                period2_Mode='F'
                period3_Mode='3O'
                period4_Mode='1O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0



        elif period2>period4>period3>period1:
            ratio1=period4/period2
            ratio2=period3/period4
            ratio3=period1/period3
            ratio4=period3/period2
            ratio5=period1/period4
            ratio6=period1/period2
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='3O'
                period2_Mode='F'
                period3_Mode='2O'
                period4_Mode='1O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


                            
        elif period3>period1>period2>period4:
            ratio1=period1/period3
            ratio2=period2/period1
            ratio3=period4/period2
            ratio4=period2/period3
            ratio5=period4/period1
            ratio6=period4/period3
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='1O'
                period2_Mode='2O'
                period3_Mode='F'
                period4_Mode='3O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1

                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


                            
        elif period3>period1>period4>period2:
            ratio1=period1/period3
            ratio2=period4/period1
            ratio3=period2/period4
            ratio4=period4/period3
            ratio5=period2/period1
            ratio6=period2/period3
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='1O'
                period2_Mode='3O'
                period3_Mode='F'
                period4_Mode='2O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0

                            
        elif period3>period2>period1>period4:
            ratio1=period2/period3
            ratio2=period1/period2
            ratio3=period4/period1
            ratio4=period1/period3
            ratio5=period4/period2
            ratio6=period4/period3
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='2O'
                period2_Mode='1O'
                period3_Mode='F'
                period4_Mode='3O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


                            
        elif period3>period2>period4>period1:
            ratio1=period2/period3
            ratio2=period4/period2
            ratio3=period1/period4
            ratio4=period4/period3
            ratio5=period1/period2
            ratio6=period1/period3
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='3O'
                period2_Mode='1O'
                period3_Mode='F'
                period4_Mode='2O'

            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0

                                 
        elif period3>period4>period1>period2:
            ratio1=period4/period3
            ratio2=period1/period4
            ratio3=period2/period1
            ratio4=period1/period3
            ratio5=period2/period4
            ratio6=period2/period3
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='2O'
                period2_Mode='3O'
                period3_Mode='F'
                period4_Mode='1O'
            
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


        elif period3>period4>period2>period1:
            ratio1=period4/period3
            ratio2=period2/period4
            ratio3=period1/period2
            ratio4=period2/period3
            ratio5=period1/period4
            ratio6=period1/period3

            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='3O'
                period2_Mode='2O'
                period3_Mode='F'
                period4_Mode='1O'

            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


        elif period4>period1>period2>period3:
            ratio1=period1/period4
            ratio2=period2/period1
            ratio3=period3/period2
            ratio4=period2/period4
            ratio5=period3/period1
            ratio6=period3/period4
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='1O'
                period2_Mode='2O'
                period3_Mode='3O'
                period4_Mode='F'

            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


        elif period4>period1>period3>period2:
            ratio1=period1/period4
            ratio2=period3/period1
            ratio3=period2/period3
            ratio4=period3/period4
            ratio5=period2/period1
            ratio6=period2/period4

            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='1O'
                period2_Mode='3O'
                period3_Mode='2O'
                period4_Mode='F'

            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0




        elif period4>period2>period1>period3:
            ratio1=period2/period4
            ratio2=period1/period2
            ratio3=period3/period1
            ratio4=period1/period4
            ratio5=period3/period2
            ratio6=period3/period4

            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='2O'
                period2_Mode='1O'
                period3_Mode='3O'
                period4_Mode='F'

            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0

  

        elif period4>period2>period3>period1:
            ratio1=period2/period4
            ratio2=period3/period2
            ratio3=period1/period3
            ratio4=period3/period4
            ratio5=period1/period2
            ratio6=period1/period4

            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='3O'
                period2_Mode='1O'
                period3_Mode='2O'
                period4_Mode='F'

            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0



        elif period4>period3>period1>period2:
            ratio1=period3/period4
            ratio2=period1/period3
            ratio3=period2/period1
            ratio4=period1/period4
            ratio5=period2/period3
            ratio6=period2/period4
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='2O'
                period2_Mode='3O'
                period3_Mode='1O'
                period4_Mode='F'
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0



        else:
            ratio1=period3/period4
            ratio2=period2/period3
            ratio3=period1/period2
            ratio4=period2/period4
            ratio5=period1/period3
            ratio6=period1/period4
            if 0.9>ratio3>ratio2>ratio1>ratio5>ratio4>ratio6>0.4 and 0.74<ratio1<0.82 and 0.76<ratio2<0.86 and 0.80<ratio3<0.88 and  0.59<ratio4<0.66 and  0.63<ratio5<0.72 and 0.46<ratio6<0.58:
                period1_Mode='3O'
                period2_Mode='2O'
                period3_Mode='1O'
                period4_Mode='F'
            else:
                period1_vb,period2_vb,period3_vb=fm3f.triplemodediscern(period1,period2,period3)
                dsdt_count1=0
                if period1_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period2_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1
                if period3_vb in ['F', '1O', '2O', '3O']:
                    dsdt_count1 +=1


                period1_qq,period2_qq,period4_qq=fm3f.triplemodediscern(period1,period2,period4)
                dsdt_count2=0
                if period1_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period2_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
                if period4_qq in ['F', '1O', '2O', '3O']:
                    dsdt_count2 +=1
 

                period1_ww,period3_ww,period4_ww=fm3f.triplemodediscern(period1,period3,period4)
                dsdt_count3=0
                if period1_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period3_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1
                if period4_ww in ['F', '1O', '2O', '3O']:
                    dsdt_count3 +=1


                period1_we,period3_we,period4_we=fm3f.triplemodediscern(period2,period3,period4)
                dsdt_count4=0
                if period1_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period3_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1
                if period4_we in ['F', '1O', '2O', '3O']:
                    dsdt_count4 +=1


                if max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count1:
                   period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)
                   period4_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count2:
                   period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)
                   period3_Mode=0
                elif max(dsdt_count1, dsdt_count2, dsdt_count3, dsdt_count4)==dsdt_count3:
                    period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)
                    period2_Mode=0
                else:
                    period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
                    period1_Mode=0


                            
    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0:
        period4_Mode=0
        period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)

    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1:
        period3_Mode=0
        period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)

    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==1:
        period2_Mode=0
        period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)

    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1:
        period1_Mode=0
        period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)
    

    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0:
        period3_Mode=0
        period4_Mode=0
        period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)

    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0:
        period2_Mode=0
        period4_Mode=0
        period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)

    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1:
        period2_Mode=0
        period3_Mode=0
        period1_Mode,period4_Mode=fm2f.doubleModediscern(period1,period4)

    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0:
        period1_Mode=0
        period4_Mode=0
        period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)
    
    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1:
        period1_Mode=0
        period3_Mode=0
        period2_Mode,period4_Mode=fm2f.doubleModediscern(period2,period4)
    
    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1:
        period1_Mode=0
        period2_Mode=0
        period3_Mode,period4_Mode=fm2f.doubleModediscern(period3,period4)
    
    else:
        period1_Mode=0
        period2_Mode=0
        period3_Mode=0
        period4_Mode=0
       


    return period1_Mode,period2_Mode,period3_Mode,period4_Mode