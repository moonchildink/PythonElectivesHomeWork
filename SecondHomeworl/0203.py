import string
"""
统计一段英文文章中每个字母（区分大小写）及数字的字符的个数，以字典形式表示，键为字母或数字，值为数量。英文文章可用文本编辑器打开，复制粘贴到Python中，写成三引号多行字符串。
"""

Article= """
It is rare for Donald Trump to deliver the same message as Barack Obama and Joe Biden - but it happened when the Republican and two Democrats campaigned in Pennsylvania on the same day.

The political foes all urged Americans in the crucial state: go vote.

Mr Biden and Mr Obama cast the election as a battle for democracy, while Mr Trump said the country's safety and security were on the line.

Tuesday's US midterm elections will determine control of Congress.

All 435 seats in the House of Representatives are being contested, while 35 are up for grabs in the Senate.

In Pennsylvania a razor-thin margin separates Democratic Senate candidate John Fetterman, 53, from Republican Mehmet Oz, 62. The appearances of two ex-presidents and President Biden on the last weekend before the election signalled the state's importance.

Mr Trump's victory in Pennsylvania helped deliver him the White House in 2016, when his message of populist anger struck a chord with blue-collar voters in the state.

An opposing sentiment of pragmatism and liberal politics in urban centres gave it back to Democrats in 2020, when Mr Biden won his home state by a margin of less than 2%.

Speaking in Philadelphia on Saturday, Mr Biden declared that it was "good to be home" as he stumped for Mr Fetterman and Josh Shapiro, the Democratic candidate for governor.

He warned the crowd that failing to return Democratic majorities in the House of Representatives and the Senate would mean further restrictions to abortion rights and cuts to public healthcare.


Media caption,
WATCH: Biden vows to veto any abortion ban attempts by Republicans

Though Democrats currently hold both chambers of Congress, they are expected to lose the House and are in a dead heat for control of the Senate, according to polls.

"Here in Philadelphia, a place that defines the soul of America, today we face an inflection point," Mr Biden said. A vote for Democrats would be a vote for women's health, gun control and healthcare, he said.

Outside the rally, voters queued early to see two presidents - Mr Biden and his Democratic predecessor Mr Obama - on the same stage.

One Pennsylvanian, Steve Phillips, told the BBC's Sarah Smith he hoped it would get people out to vote, regardless which party they supported.

But some of the crowd admitted it was really Mr Obama they had come to see, and they might not have turned up if Mr Biden had been here alone.

Midterms are often seen as a referendum on the sitting president, and with Mr Biden's approval hovering at 40%, Republicans have found plenty to criticise as Americans worry about high inflation, guns and immigration.

As it happened: Pennsylvania rallies
Five reasons why US midterm elections matter
What Trump is hoping for on election night
US midterms 2022: A simple guide
Some 250 miles (402km) west of Philadelphia, Mr Trump warned Pennsylvanians in the small town of Latrobe that continued Democratic control in Washington would lead to more crime and unfettered immigration.

Supporters there, too, gathered hours early to see Mr Trump.


Media caption,
Watch: Trump criticises Biden and hints 2024 run at rally

"If you want safety and security for your family, you need to vote every single Democrat out of office," he said.

"There's only one choice - if you support the decline and fall of America then you must vote for the radical Democrats. If you want to stop the destruction of our country then you must vote Republican in a giant red wave."

The former Republican president also hinted again at the possibility of running for office in 2024 - even as he has continued to make false claims that the US election system is fraudulent. "The election was rigged and stolen - it's a shame," Mr Trump said.

One attendee told RSBN, a conservative network, that he was there to support Mr Trump because the former president had helped ensure that people could "live a life without suppression and being told what we need to do".

Fears and false claims of fraud have haunted these midterms, with many arguing that the 8 November vote will be a test of the fidelity of the election system.

Back in Philadelphia, taking the marquee speaking slot after Mr Biden, Mr Obama warned: "Truth and facts and logic and reason and basic decency are on the ballot. Democracy itself is on the ballot - the stakes are high".
"""


def Static(s):
    dictionary = dict()
    dictionary['letters'] = 0
    dictionary['nums'] = 0
    for i in map(s.count,string.ascii_letters):
        dictionary['letters'] = dictionary['letters'] + i
    for i in map(s.count,''.join(map(str,range(10)))):
        dictionary['nums'] +=i
    return dictionary


print(Static(Article))