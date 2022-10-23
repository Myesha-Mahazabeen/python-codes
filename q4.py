# Myesha Mahazabeen, EMPLID: 24005884

def freeTime(workTime, meetings):
    tm = workTime[0]
    freeTimes = []
    frtm = [tm]
    while tm!=workTime[1]:
        if len(meetings)!=0 and meetings[0][0]==tm:
            frtm.append(tm)
            if frtm[0]!=frtm[1]:
                freeTimes.append(frtm)
            frtm = [meetings[0][1]]
            tm = meetings[0][1]
            meetings= meetings[1:]
        else:
            if tm[3:]=='50':
                tm = str(int(tm[:2])+1)+':00'
                if len(tm)<5:
                    tm = '0'+tm
            else:
                tm = tm[0:3]+str(int(tm[3:])+10)
            
    frtm.append(workTime[1])
    if frtm[0]!=frtm[1]:
        freeTimes.append(frtm)
    return freeTimes

def commonFreeTime(ft1, ft2):
    m_times = []
    for tm1 in ft1:
        for tm2 in ft2:
            if max(tm1[0], tm2[0])<min(tm1[1], tm2[1]):
                cmn_tm = [max(tm1[0], tm2[0]), min(tm1[1], tm2[1])]
                m_times.append(cmn_tm)
    return m_times

BobMeetings = [[ '09:00' ,'10:30' ],[ '11:00' , '12:00'],['13:00','14:30'] ,['15:30','17:00']] 
BobWorkHours = ['07:00','18:00']

AliceMeetings = [[ '08:00' ,'09:30' ],[ '09:30' ,'11:00'],['13:00','14:00'] ,['15:00','16:30']]
AliceWorkHours = ['07:00','19:00']

AliceFreeTime = freeTime(AliceWorkHours, AliceMeetings)
BobFreeTime = freeTime(BobWorkHours, BobMeetings) 

print('Available times: ', commonFreeTime(AliceFreeTime, BobFreeTime))
