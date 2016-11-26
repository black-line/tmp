import string
ms = ['01','02','03','04','05','06','07','08','09','10','11','12']
l = [str(x) for x in range(10,32)]
ds = ['01','02','03','04','05','06','07','08','09'] + l

out_filename = '/home/watermelon/Downloads/uv/out.txt'#!!!

for year in range(1985,2004):#!!!
    for month in ms:

        l_lines = []
        dbg_file_name = ''
        for days in ds:
            try:
                file_name = r'/home/watermelon/Downloads/uv/sbuv_n09_1997/sbuv_n09_'+str(year)+month+days+ '.txt'   #!!!

                dbg_file_name = file_name
                uv_file = open(file_name)

                tmp_lines = uv_file.readlines()
                #print tmp_lines
                l_lines += tmp_lines[8:]
                uv_file.close()


                #print file_name
            except:
                pass

        #single month data in l_lines


        cnt = 0

        #a 0-30 b 30-60 c 60-90 d 0--30 e -30--60 f -60--90
        a = b = c = d = e = f = 0
        cnt_a = cnt_b = cnt_c = cnt_d = cnt_e = cnt_f = 0
        for aline in l_lines:
            # select one line per three lines

            if cnt % 3 ==0:

                ls = aline.split()
                year = ls[0]
                day = ls[1]
                Lat = string.atof(ls[3])
                Lon = ls[4]
                TO = string.atof(ls[6])
                if 0 < Lat < 30:
                    a += TO
                    cnt_a += 1
                elif 30 < Lat < 60:
                    b += TO
                    cnt_b += 1
                elif 60 < Lat < 90:
                    c += TO
                    cnt_c += 1
                elif -30 < Lat < 0:
                    d += TO
                    cnt_d += 1
                elif -60 < Lat < -30:
                    e += TO
                    cnt_e += 1
                elif -90 < Lat < -60:
                    f += TO
                    cnt_f += 1

            cnt += 1
        try:
            a = a / cnt_a
        except:
            pass
        try:
            b = b / cnt_b
        except:
            pass
        try:
            c = c / cnt_c
        except:
            pass
        try:
            d = d / cnt_d
        except:
            pass
        try:
            e = e / cnt_e
        except:
            pass
        try:
            f = f / cnt_f
        except:
            pass
        #print dbg_file_name
        #print a,b,c,d,e,f
        #print cnt_a,cnt_b,cnt_c,cnt_d,cnt_e,cnt_f
        out_list = str(year)+','+str(month)+','+str(a)+','+str(b)+','+str(c)+','+str(d)+','+str(e)+','+str(f)+'\n'
        out = open(out_filename,'a')
        out.write(out_list)
        out.close()
        print year,month,a,b,c,d,e,f


