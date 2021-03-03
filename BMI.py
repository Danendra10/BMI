#menghitung body mass index (BMI)

massa = float(input('Masukkan berat badan anda (kg):'))
tinggi = float(input('Masukkan tinggi (m):'))

bmi = massa/(tinggi*tinggi)

print('BMI anda adalah:', str(bmi))

if bmi < 18.5:
    print('Anda terlalu kurus')
elif bmi < 25:
    print ('Anda normal')
elif bmi < 30:
    print ('Anda gemuk')
else:
    print ('Anda terlalu gemuk')
