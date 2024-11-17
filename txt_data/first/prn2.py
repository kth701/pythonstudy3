
print("-- 출력 형식")
print("1. 정수")

output_a = "형식1. 정수: |{:d}|".format(52)
print(output_a)
output_b = "형식2. 정수: |{:10d}|".format(52)
print(output_b)
output_c = "형식3. 정수: |{:010d}|".format(52)
print(output_c)
output_d = "형식4. 정수: |{:010d}|".format(-52)
print(output_d)
print("---")
output_e = "형식5. 정수: |{:+d}|".format(52)
print(output_e)
output_f = "형식6. 정수: |{: d}|".format(-52)
print(output_f)
output_g = "형식7. 정수: |{:+10d}|".format(52)
print(output_g)
output_h = "형식8. 정수: |{:=+10d}|".format(52)
print(output_h)

print("2. 실수")
output_f1 = "실수형 형식1. |{:f}|".format(52.273)
print(output_f1)
output_f2 = "실수형 형식2. |{:15f}|".format(52.273)
print(output_f2)
output_f3 = "실수형 형식3. |{:+015f}|".format(52.273)
print(output_f3)
output_f4 = "실수형 형식4. [{:15.2f}]".format(52.273)
print(output_f4)
output_f5 = "실수형 형식4. [{:g}]".format(52.000)
print(output_f5)

