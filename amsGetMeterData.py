#!/usr/bin/env python
import time
import serial
import datetime
import math

ser = serial.Serial(
        port='/dev/serial0',
        baudrate = 2400,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

#Defenition
#Number is one unit/one number
#Value consist of several numbers

#Global variable
#Define array for hex values inn telegram (max 140 bytes)
hex_byte_array = [ \
"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00",
"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00",
"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00",
"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00",
"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00",
"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00",
"00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"]


def decNumberConvertToStr(dec_Number):
    #dec number convert to string format 00...09
    str_Number = "00"
    if dec_Number >= 0 and dec_Number <=9:
       str_Number_buf = str(dec_Number)
       str_Number = "0" + str_Number_buf
    else:
       str_Number = str(dec_Number)
    return str_Number


def hexValue4ByteConvertToDecValue(hex_value):
    #Convert hex to dec integer - ex. int("a", 16) = 10
    dec_value = 0
    hexV0 = int(hex_value[7:8],16)
    hexV1 = int(hex_value[6:7],16)
    hexV2 = int(hex_value[5:6],16)
    hexV3 = int(hex_value[4:5],16)
    hexV4 = int(hex_value[3:4],16)
    hexV5 = int(hex_value[2:3],16)
    hexV6 = int(hex_value[1:2],16)
    hexV7 = int(hex_value[0:1],16)
    #print  hexV0,hexV1,hexV2,hexV3,hexV4,hexV5,hexV6,hexV7
    dec_value = hexV7*pow(16,7)+hexV6*pow(16,6)+hexV5*pow(16,5)+hexV4*pow(16,4)+hexV3*pow(16,3)+ \
                hexV2*pow(16,2)+hexV1*pow(16,1)+hexV0*pow(16,0)
    return int(dec_value)


def hexValue2ByteConvertToDecValue(hex_value):
    dec_value = 0
    hexV0 = int(hex_value[3:4],16)
    hexV1 = int(hex_value[2:3],16)
    hexV2 = int(hex_value[1:2],16)
    hexV3 = int(hex_value[0:1],16)
    dec_value = hexV3*pow(16,3)+hexV2*pow(16,2)+hexV1*pow(16,1)+hexV0*pow(16,0)
    return int(dec_value)


def hexValue1ByteConvertToDecValue(hex_value):
    dec_value = 0
    hexV0 = int(hex_value[1:2],16)
    hexV1 = int(hex_value[0:1],16)
    dec_value = hexV1*pow(16,1)+hexV0*pow(16,0)
    return int(dec_value)

def convert4hexToDec(pos1,pos2,pos3,pos4):
    hex_value = hex_byte_array[int(pos1)]+hex_byte_array[int(pos2)]+hex_byte_array[int(pos3)]+ \
                hex_byte_array[int(pos4)]
    dec_value = hexValue4ByteConvertToDecValue(hex_value)
    return dec_value

def convert2hexToDec(pos1,pos2):
    hex_value = hex_byte_array[int(pos1)]+hex_byte_array[int(pos2)]
    dec_value = hexValue2ByteConvertToDecValue(hex_value)
    return dec_value

def convert1hexToDecXX(pos1):
    hex_value = hex_byte_array[int(pos1)]
    dec_value = hexValue1ByteConvertToDecValue(hex_value)
    dec_value_XX = decNumberConvertToStr(dec_value)
    return dec_value_XX

def readTelegram2SecondListe1():
    #---read 2 seconds telegram, 39-2=37 hexbytes into array---
    #---Number is byte position in telegram---
    for i in range(37):
       hex_byte_array[i+3] = str(ser.read().encode('hex'))
    #---Time stamp part YYYYMMDDHHMMSS---
    year   = convert2hexToDec(19,20)
    month  = convert1hexToDecXX(21)
    date   = convert1hexToDecXX(22)
    day    = convert1hexToDecXX(23)
    hour   = convert1hexToDecXX(24)
    minute = convert1hexToDecXX(25)
    second = convert1hexToDecXX(26)
    time_stamp = str(year)+month+date+hour+minute+second
    #---Activ Power---
    activ_power_pos = convert4hexToDec(34,35,36,37)
    return time_stamp, activ_power_pos


def readTelegram10SecondListe2():
    #---read 10 seconds telegram, 101-2=99 hexbytes into array---
    #---Number  is byte position in telegram---
    for i in range(99):
       hex_byte_array[i+3] = str(ser.read().encode('hex'))
       #print i+3, hex_byte_array[i+3]
    #---Time stamp part  YYYYMMDDHHMMSS---
    year   = convert2hexToDec(19,20)
    month  = convert1hexToDecXX(21)
    date   = convert1hexToDecXX(22)
    day    = convert1hexToDecXX(23)
    hour   = convert1hexToDecXX(24)
    minute = convert1hexToDecXX(25)
    second = convert1hexToDecXX(26)
    time_stamp = str(year)+month+date+hour+minute+second
    #---Meter values---
    activ_power_pos   = convert4hexToDec(71,72,73,74)
    activ_power_neg   = convert4hexToDec(76,77,78,79)
    reactiv_power_pos = convert4hexToDec(81,82,83,84)
    reactiv_power_neg = convert4hexToDec(86,87,88,89)
    current_L1        = convert4hexToDec(91,92,93,94)
    voltage_L1        = convert4hexToDec(96,97,98,99)
    return time_stamp,activ_power_pos,activ_power_neg,reactiv_power_pos,reactiv_power_neg, \
           current_L1,voltage_L1

def readTelegram1HourListe3():
    #---Telegram is sent 10 sec after hour  shift---
    #---read 1 hour telegram, 135-2=133 hexbytes into array---
    #---Number  is byte position in telegram---
    for i in range(133):
       hex_byte_array[i+3] = str(ser.read().encode('hex'))
    #---Time stamp meter data  YYYYMMDDHHMMSS---
    year   = convert2hexToDec(19,20)
    month  = convert1hexToDecXX(21)
    date   = convert1hexToDecXX(22)
    day    = convert1hexToDecXX(23)
    hour   = convert1hexToDecXX(24)
    minute = convert1hexToDecXX(25)
    second = convert1hexToDecXX(26)
    time_stamp = str(year)+month+date+hour+minute+second
    #---Time stamp energy  YYYYMMDDHHMMSS---
    year   = convert2hexToDec(102,103)
    month  = convert1hexToDecXX(104)
    date   = convert1hexToDecXX(105)
    day    = convert1hexToDecXX(106)
    hour   = convert1hexToDecXX(107)
    minute = convert1hexToDecXX(108)
    second = convert1hexToDecXX(109)
    time_stamp_energy = str(year)+month+date+hour+minute+second
    #---Meter values---
    activ_power_pos    = convert4hexToDec(71,72,73,74)
    activ_power_neg    = convert4hexToDec(76,77,78,79)
    reactiv_power_pos  = convert4hexToDec(81,82,83,84)
    reactiv_power_neg  = convert4hexToDec(86,87,88,89)
    current_L1         = convert4hexToDec(91,92,93,94)
    voltage_L1         = convert4hexToDec(96,97,98,99)
    activ_energy_pos   = convert4hexToDec(115,116,117,118)
    activ_energy_neg   = convert4hexToDec(120,121,122,123)
    reactiv_energy_pos = convert4hexToDec(125,126,127,128)
    reactiv_energy_neg = convert4hexToDec(130,131,132,133)
    return time_stamp,activ_power_pos,activ_power_neg,reactiv_power_pos,reactiv_power_neg, \
           current_L1,voltage_L1,activ_energy_pos,activ_energy_neg,reactiv_energy_pos,reactiv_energy_neg, \
           time_stamp_energy


while 1:

    hex_byte = ser.read().encode('hex')

    #Start byte for a new telegram if next byte is A0
    if hex_byte == "7e":
        hex_byte = ser.read().encode('hex')
        #---Ready for a new telegram---
        if hex_byte == "a0":
            hex_byte = ser.read().encode('hex')
            #---Telegram 2 second, Liste1---
            if hex_byte == "27":    #27h=39d telegram length between 7e-7e
                #---Read telegram data---
                time_stamp,activ_power_pos = readTelegram2SecondListe1()
                #---Save present value activ power 2 sec---
                file_ams = open("ams_activ_power_pos_2sec.dat","w") 
                file_ams.writelines("%14s %6s %2s\n" % (time_stamp, str(activ_power_pos),"W+"))
                file_ams.close()

            #---Telegram 10 second, Liste2---
            if hex_byte == "65":    #65h=101d telegram length between 7e-7e
                #---Read telegram data---
                time_stamp,activ_power_pos,activ_power_neg,reactiv_power_pos,reactiv_power_neg,current_L1, \
                     voltage_L1 \
                     = readTelegram10SecondListe2()
                #print tid,time_stamp,activ_power_pos,"W+ ",activ_power_pos,"W- ",reactiv_power_neg,"VAr+ ", \
                #      reactiv_power_neg,"VAr- ",current_L1,"mA ",voltage_L1,"Vx10 "
                #---Write to logg file every 10 sec---
                #---Save present value activ power 2 sec---
                file_ams = open("ams_activ_power_pos_2sec.dat","w") 
                file_ams.writelines("%14s %6s %2s\n" % (time_stamp, str(activ_power_pos),"W+"))
                file_ams.close()
                #---Save present meter values 10 sec---
                file_ams = open("ams_meter_value_10sec.dat","w") 
                file_ams.writelines("%14s %6s %2s %6s %2s %6s %4s %6s %4s %6s %2s %6s %4s\n" % \
                     (time_stamp, \
                     activ_power_pos,"W+", activ_power_neg,"W-", \
                     reactiv_power_pos,"VAr+", reactiv_power_neg,"VAr-", \
                     current_L1,"mA", voltage_L1,"Vx10"))
                file_ams.close()
                #---Log meter values every 10 sec---
                file_ams = open("ams_meter_value_10sec.log","a") 
                file_ams.writelines("%14s %6s %2s %6s %2s %6s %4s %6s %4s %6s %2s %6s %4s\n" % \
                     (time_stamp, \
                     activ_power_pos,"W+", activ_power_neg,"W-", \
                     reactiv_power_pos,"VAr+", reactiv_power_neg,"VAr-", \
                     current_L1,"mA", voltage_L1,"Vx10"))
                file_ams.close()

            #---Telegram 1 hour, Liste3---
            if hex_byte == "87":    #87h=135d telegram length between 7e-7e
                #---Read telegram data---
                time_stamp,activ_power_pos,activ_power_neg,reactiv_power_pos,reactiv_power_neg,current_L1, \
                    voltage_L1,activ_energy_pos,activ_energy_neg,reactiv_energy_pos,reactiv_energy_neg, \
                    time_stamp_energy \
                    = readTelegram1HourListe3()
                #print tid,time_stamp,activ_power_pos,"W+ ",activ_power_pos,"W- ",reactiv_power_neg,"VAr+ ", \
                #      reactiv_power_neg,"VAr- ",current_L1,"mA ",voltage_L1,"Vx10 ",activ_energy_pos,"Wh"
                #---Write to logg file every 1 hour---
                #---Save present value activ power 2 sec---
                file_ams = open("ams_activ_power_pos_2sec.dat","w") 
                file_ams.writelines("%14s %6s %2s\n" % (time_stamp, str(activ_power_pos),"W+"))
                file_ams.close()
                #---Save present meter values 10 sec---
                file_ams = open("ams_meter_value_10sec.dat","w") 
                file_ams.writelines("%14s %6s %2s %6s %2s %6s %4s %6s %4s %6s %2s %6s %4s\n" % \
                     (time_stamp, \
                     activ_power_pos,"W+", activ_power_neg,"W-", \
                     reactiv_power_pos,"VAr+", reactiv_power_neg,"VAr-", \
                     current_L1,"mA", voltage_L1,"Vx10"))
                file_ams.close()
                #---Log meter values every 10 sec---
                file_ams = open("ams_meter_value_10sec.log","a") 
                file_ams.writelines("%14s %6s %2s %6s %2s %6s %4s %6s %4s %6s %2s %6s %4s\n" % \
                     (time_stamp, \
                     activ_power_pos,"W+", activ_power_neg,"W-", \
                     reactiv_power_pos,"VAr+", reactiv_power_neg,"VAr-", \
                     current_L1,"mA", voltage_L1,"Vx10"))
                file_ams.close()
                #---Save last hour energy  1 hour---
                file_ams = open("ams_meter_energy_1hour.dat","w") 
                file_ams.writelines("%14s %10s %3s %10s %3s %10s %5s %10s %5s\n" % \
                     (time_stamp_energy, \
                     activ_energy_pos,"Wh+",activ_energy_neg,"Wh-",reactiv_energy_pos,"VArh+",reactiv_energy_neg,"VArh-"))
                file_ams.close()
                #---Log meter energy every 1 hour---
                file_ams = open("ams_meter_energy_1hour.log","a") 
                file_ams.writelines("%14s %10s %3s %10s %3s %10s %5s %10s %5s\n" % \
                     (time_stamp_energy, \
                     activ_energy_pos,"Wh+",activ_energy_neg,"Wh-",reactiv_energy_pos,"VArh+",reactiv_energy_neg,"VArh-"))
				file_ams.close()