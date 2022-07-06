f = open('digi_ps2.bin', 'w+b')
array = [116,10,3,100,7,26,55,97,14,255,111,19,255,68,84,255,255,177,81,90,255,255,2,3,4,5,93,255,255,9,9]
binary_format = bytearray(array)
f.write(binary_format)
f.close()
