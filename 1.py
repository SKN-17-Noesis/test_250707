with open("input.txt", "r", encoding="utf-8") as f:
    l = f.read().strip().split(" ")
    
with open("output.txt", "w", encoding="utf-8") as f:
    s = float(l[0])
    t = float(l[1])
    
    speed_d = s / 150.0
    dis_d = speed_d * t
    
    f.write(f"{dis_d:.2f}")