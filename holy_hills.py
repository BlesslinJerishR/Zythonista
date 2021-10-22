m_rain = True
a_rain = True
l_afternoon = True
c_morning = True

if(m_rain):
    l_afternoon
    print("The Afternoon is Lovely")
if(a_rain):
    c_morning
    print("Its a Clear Morning")

x,y,z = 0,0,0;

rm_la = x;
cm_ra = y;
nm_na = z;

days_rain = 13          # x+y 
nice_mornings = 12      # y+z
nice_afternoons = 11    # x+z

# Common 2(x+y+z)
total_holidays = (days_rain + nice_mornings + nice_afternoons) / 2 ;
print("Total holidays spent is : ", int(total_holidays) ," Days ");