def get_data (file):
    registers = {}
    instructions = []
    for i, line in enumerate (file):
        if i == 3:
            continue
        if i < 3:
            if i == 0:
                registers["A"] = int(line.strip().split(":")[1].strip())
            elif i == 1:
                registers["B"] = int(line.strip().split(":")[1].strip())
            elif i == 2:
                registers["C"] = int(line.strip().split(":")[1].strip())
        else:
            instructions = line.strip().split(":")[1].strip().split(",")
    instructions = list (map (int, instructions))
    return registers, instructions

def calc_coperands (regs, operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return regs["A"]
    elif operand == 5:
        return regs["B"]
    elif operand == 6:
        return regs["C"]
    else:
        return -1

def adv (regs, operand):
    combo_operand = calc_coperands (regs, operand)
    regs["A"] = int (regs["A"]/(2**combo_operand))

def bxl (regs, operand):
    regs["B"] = regs["B"] ^ operand

def bst (regs, operand):
    combo_operand = calc_coperands (regs, operand)
    regs["B"] = combo_operand % 8

def jnz (regs, operand, ip):
    if regs["A"] != 0:
        return operand
    return ip + 2
  
def bxc (regs, operand):
    regs["B"] = regs["B"] ^ regs["C"]

def out (regs, operand):
    combo_operand = calc_coperands (regs, operand)
    return str(combo_operand % 8)

def bdv (regs, operand):
    combo_operand = calc_coperands (regs, operand)
    regs["B"] = int (regs["A"]/(2**combo_operand))

def cdv (regs, operand):
    combo_operand = calc_coperands (regs, operand)
    regs["C"] = int (regs["A"]/(2**combo_operand))

def run_instructions (regs, cmds, p2 = False, target = None):
    ip = 0
    output = ""
    while True:
        try:
            cmd = cmds[ip]
            operand = cmds[ip + 1]
        except IndexError:
            break

        if cmd == 0:
            adv (regs, operand)
        elif cmd == 1:
            bxl (regs, operand)
        elif cmd == 2:
            bst (regs, operand)
        elif cmd == 3:
            ip = jnz (regs, operand, ip)
            continue
        elif cmd == 4:
            bxc (regs, operand)
        elif cmd == 5:
            output += out (regs, operand) + ","
        elif cmd == 6:
            bdv (regs, operand)
        elif cmd == 7:
            cdv (regs, operand)
        ip += 2

        if p2:
            if output != "":
                #print(target.find(output))
                if target.find(output) != 0:
                    return False
    if output:
        print(output[:-1])
    if p2:
        return output == target
    
    


if __name__ == "__main__":
    with open ("p17_input.txt", "r", encoding = "utf-8") as file:
        regs, cmds = get_data (file)
        

    #print(regs)
    #print(cmds)
    t = ""
    for x in cmds:
        t += str(x) + "," 

    # p2 stuff
    print(t)
    for x in range (100000000, 1000000000):
        regs["A"] = x
        if run_instructions (regs, cmds, p2 = True, target = t):
            break 
        print(x)
    print(x)
    #print(regs)
