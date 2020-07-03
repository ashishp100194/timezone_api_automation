from BaseClass import BaseClass
from Variables import Variables

def test_List_Time_Zone_TC1():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC1")

def test_List_Time_Zone_TC2():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC2")

def test_List_Time_Zone_TC3():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC3")

def test_List_Time_Zone_TC4():
    Base = BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC4",Variables["api_base_url"], Variables['Invalid_Key'])

def test_List_Time_Zone_TC5():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC5")

def test_List_Time_Zone_TC6():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC6")

def test_List_Time_Zone_TC7():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC7")

def test_List_Time_Zone_TC8():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC8")

def test_List_Time_Zone_TC9():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC9")

def test_List_Time_Zone_TC10():
    Base=BaseClass()
    Base.Timezone("List_Time_Zone", "List_Time_Zone_TC10")

def execute_List_Time_Zone():
    test_List_Time_Zone_TC1()
    test_List_Time_Zone_TC2()
    test_List_Time_Zone_TC3()
    test_List_Time_Zone_TC4()
    test_List_Time_Zone_TC5()
    test_List_Time_Zone_TC6()
    test_List_Time_Zone_TC7()
    test_List_Time_Zone_TC8()
    test_List_Time_Zone_TC9()
    test_List_Time_Zone_TC10()

execute_List_Time_Zone()