tubemap = {
#green line
"Pasir ris" : {"Tampines":2},
"Tampines": {"Simei":2, "Pasir ris":2,"75009:72":2},
"Simei": {"Taneh Merah":2, "Tampines":2},
"Taneh Merah":{"Simei":2, "Changi Airport":2,"Bedok":2},
"Bedok":{"Kembangan":2,"Taneh Merah":2},
"Kembangan":{"Eunos":2, "Bedok":2},
"Eunos":{"Paya Lebar":2, "Kembangan":2},
"Paya Lebar":{"Aljunied":2, "Eunos":2},
"Aljunied":{"Kallang":2, "Paya Lebar":2},
"Kallang":{"Lavender":2, "Aljunied":2},
"Lavender":{"Bugis":2, "Kallang":2},
"Bugis":{"City Hall":2, "Lavender":2},
"City Hall":{"Raffles Place":2, "Bugis":2,"Dhoby Ghaut":2},
"Raffles Place":{"Tanjong Pagar":2, "City Hall":2, "Marina Bay":2},
"Tanjong Pagar":{"Outram Park":2, "Raffles Place":2},
"Outram Park":{"Tiong Bahru":2, "Tanjong Pagar":2},
"Tiong Bahru":{"Redhill":2, "Outram Park":2},
"Redhill": {"Queenstown":2, "Tiong Bahru":2},
"Queenstown": {"Commonwealth":2, "Redhill":2},
"Commonwealth":{"Buona Vista":2, "Queenstown":2},
"Buona Vista":{"Dover":2,"Commonwealth":2},
"Dover":{"Clementi":2, "Buona Vista":2},
"Clementi":{"Jurong East":2, "Dover":2},
"Jurong East":{"Chinese Garden":2, "Clementi":2,"Bukit Batok":2},
"Chinese Garden":{"Lakeside":2, "Jurong East":2},
"Lakeside":{"Boon Lay":2, "Chinese Garden":2},
"Boon Lay":{"Pioneer":2, "Lakeside":2},
"Pioneer":{"Joo Koon":2, "Boon Lay":2},
"Joo Koon":{"Pioneer":2},

#red line
"Marina South Pier":{"Marina Bay":2,},
"Marina Bay":{"Raffles Place":2, "Marina South Pier":2},
"Dhoby Ghaut":{"City Hall":2, "Somerset":2},
"Somerset":{"Orchard":2, "Dhoby Ghaut":2},
"Orchard":{"Newton":2, "Somerset":2},
"Newton":{"Novena":2, "Orchard":2},
"Novena":{"Toa Payoh":2, "Newton":2},
"Toa Payoh":{"Braddell":2, "Novena":2},
"Braddell":{"Bishan":2, "Toa Payoh":2},
"Bishan":{"Ang Mo Kio":2, "Braddell":2},
"Ang Mo Kio":{"Yio Chu Kang":2, "Bishan":2},
"Yio Chu Kang":{"Khatib":2, "Ang Mo Kio":2,"55509:72":2},
"Khatib":{"Yishun":2, "Yio Chu Kang":2},
"Yishun":{"Canberra":2, "Khatib":2},
"Canberra":{"Sembawang":2, "Yishun":2},
"Sembawang":{"Admiralty":2, "Canberra":2},
"Admiralty":{"Woodlands":2, "Sembawang":2},
"Woodlands":{"Marsiling":2, "Admiralty":2},
"Marsiling":{"Kranji":2, "Woodlands":2},
"Kranji":{"Sungei Kadut":2, "Marsiling":2},
"Sungei Kadut":{"Yew Tee":2, "Kranji":2},
"Yew Tee":{"Choa Chu Kang":2, "Sungei Kadut":2},
"Choa Chu Kang":{"Bukit Gombak":2, "Yew Tee":2},
"Bukit Gombak":{"Bukit Batok":2, "Choa Chu Kang":2},
"Bukit Batok":{"Jurong East":2, "Bukit Gombak":2},

#Bus 72 Yio Chu Kang to Tampines
"55509:72":{"Yio Chu Kang":2,"55321:72":5},
"55321:72":{"55509:72":0,"54359:72":5},  
"54359:72":{"55321:72":0,"54479:72":5},
"54479:72":{"54359:72":0,"54489:72":5},
"54489:72":{"54479:72":0,"54499:72":5},
"54499:72":{"54489:72":0,"54509:72":5},
"54509:72":{"54499:72":0,"54659:72":5},
"54659:72":{"54509:72":0,"66459:72":5},
"66459:72":{"54659:72":0,"66479:72":5},
"66479:72":{"66459:72":0,"64111:72":5},
"64111:72":{"66479:72":0,"64499:72":5},
"64499:72":{"64111:72":0,"64489:72":5},
"64489:72":{"64499:72":0,"64479:72":5},
"64479:72":{"64489:72":0,"64411:72":5},
"64411:72":{"64479:72":0,"64339:72":5},
"64339:72":{"64411:72":0,"64529:72":5},
"64529:72":{"64339:72":0,"64551:72":5},
"64551:72":{"64529:72":0,"64541:72":5},
"64541:72":{"64551:72":0,"64011:72":5},
"64011:72":{"64541:72":0,"63061:72":5},
"63061:72":{"64011:72":0,"63241:72":5},
"63241:72":{"63061:72":0,"64209:72":5},
"64209:72":{"63241:72":0,"64219:72":5},
"64219:72":{"64209:72":0,"64229:72":5},
"64229:72":{"64219:72":0,"64139:72":5},
"64139:72":{"64229:72":0,"64149:72":5},
"64149:72":{"64139:72":0,"64159:72":5},
"64159:72":{"64149:72":0,"64169:72":5},
"64169:72":{"64159:72":0,"64179:72":5},
"64179:72":{"64169:72":0,"64189:72":5},
"64189:72":{"64179:72":0,"64199:72":5},
"64199:72":{"64189:72":0,"73029:72":5},
"73029:72":{"64199:72":0,"73039:72":5},
"73039:72":{"73029:72":0,"74019:72":5},
"74019:72":{"73039:72":0,"74029:72":5},
"74029:72":{"74019:72":0,"74039:72":5},
"74039:72":{"74029:72":0,"74049:72":5},
"74049:72":{"74039:72":0,"75311:72":5},
"75311:72":{"74049:72":0,"75291:72":5},
"75291:72":{"75311:72":0,"75281:72":5},
"75281:72":{"75291:72":0,"75271:72":5},
"75271:72":{"75281:72":0,"75261:72":5},
"75261:72":{"75271:72":2,"75129:72":5},
"75129:72":{"75261:72":2,"75009:72":5},
"75009:72":{"Tampines":2,"75129:72":5},



}
