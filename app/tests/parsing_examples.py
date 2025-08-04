import datetime
import zoneinfo

default_article_details = {'content': 'Several thousand Boeing defence workers were set to strike on Monday after '
                                      'rejecting the company’s latest contract offer, spelling new trouble for the '
                                      'aerospace giant.Roughly 3,200 members of the International Association of '
                                      'Machinists and Aerospace Workers (IAM) working at Boeing defence manufacturing '
                                      'facilities in the St Louis area voted to reject Boeing’s latest four-year labour'
                                      ' proposal.“A strike will begin at midnight on Monday,” the union said in a '
                                      'statement on Sunday.The workers build F-15 Eagle and F/A-18 Super Hornet '
                                      'fighter jets, as well as various missiles and munitions. Boeing’s defence'
                                      ' business, which has more than 19,000 employees, brought in about 29 per '
                                      'cent of the company’s $22.75bn second-quarter revenue.The defence unit, which'
                                      ' in March won the contract to build the US’s next generation F-47 fighter jet,'
                                      ' has been improving its performance. For the second quarter, it reported an '
                                      'operating profit of $110mn, compared with an operating loss of $913mn in the'
                                      ' same period a year earlier.Over the years, the defence business has been '
                                      'plagued by charges due to cost overruns on fixed-price contracts and production '
                                      'delays, including for two new Air Force One presidential jets.The potential work'
                                      ' stoppage comes less than a year after 33,000 workers at Boeing’s Washington '
                                      'state factories went on strike for two months, costing the company several '
                                      'billion dollars and halted production of the 737 Max commercial jet. It also '
                                      'comes as Boeing pursues a broader turnaround after the 2024 strike and the '
                                      'blowout of a door panel on an Alaska Airlines jet mid-flight that sparked '
                                      'fresh questions over its manufacturing quality and led to a regulator-imposed '
                                      'production cap on the 737 Max.An Air India crash in June which involved a '
                                      'Boeing 787-8 plane also cast a shadow over the company’s recovery efforts, '
                                      'though preliminary findings by Indian investigators recommended “no actions” '
                                      'against the company. The Missouri workers “build the aircraft and defence '
                                      'systems that keep our country safe,” said IAM Midwest territory general '
                                      'vice-president Sam Cicinelli. “They deserve nothing less than a contract '
                                      'that keeps their families secure and recognises their unmatched '
                                      'expertise.”“We’re disappointed our employees rejected an offer that '
                                      'featured 40 per cent average wage growth and resolved their primary '
                                      'issue on alternative work schedules”, said Dan Gillian, Boeing air '
                                      'dominance vice-president, in a statement. But the company brushed off'
                                      ' the potential impact of any walk off, stressing its comparatively smaller'
                                      ' scale to the 2024 strike.“We are prepared for a strike and have fully '
                                      'implemented our contingency plan to ensure our non-striking workforce can '
                                      'continue supporting our customers,” Gillian said.Boeing chief executive '
                                      'Kelly Ortberg told analysts on an earnings call on Tuesday that the company '
                                      'would “manage through this”.“The order of magnitude of this is much, much '
                                      'less than what we saw last fall\u2009.\u2009.\u2009.\u2009I wouldn’t worry '
                                      'too much about the implications of the strike”, he said, adding that any work '
                                      'stoppage would not knock Boeing off course as it aims to get its defence '
                                      'business back to high single-digit margins.The Pentagon, Boeing’s primary '
                                      'defence customer, did not immediately respond to a request for '
                                      'comment.Additional reporting by Jamie John in New York',
                           'word_count': 511,
                           'author': 'Steff Chávez',
                           'tags': ['International Association of Machinists & Aerospace Workers',
                                    'US companies', 'Kelly Ortberg', 'Boeing Company', 'Aerospace & Defence'],
                           'related_articles': []
                           }
default_article_image_url = 'https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms' \
                            '.cloudfront.net%2Fproduction%2F378c8b54-0a66-4f28-ac03-e55e2d7d1791.jpg?source' \
                            '=next-article&fit=scale-down&quality=highest&width=700&dpr=1'
visual_investigation_article = {'content': "Haiti is one of the most violent places on the planet. Armed with guns "
                                           "imported illegally from the US, gangs have turned into militias.Your"
                                           " browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser"
                                           " doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support "
                                           "HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your "
                                           "browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Your browser doesn't support HTML5 video.Brandishing military-style weapons, these groups control most of "
                                           "the capital, Port-au-Prince. The UN says they now have greater firepower "
                                           "than the Haitian police.Your browser doesn't support HTML5 video.Your "
                                           "browser doesn't support HTML5 video.Your browser doesn't support HTML5 "
                                           "video.Your browser doesn't support HTML5 video.A Financial Times "
                                           "investigation shows many of these firearms are smuggled from Florida, "
                                           "where they are easily obtained due to the state’s lax gun laws.The "
                                           "weapons are hidden in containers carrying household goods and transported "
                                           "to Haiti or neighbouring countries using loosely regulated shipping "
                                           "companies.Your browser doesn't support HTML5 video.“Be careful,"
                                           "” Jimmy “Barbecue” Cherizier, Haiti’s most powerful gang leader, "
                                           "said in a chilling message to the authorities after a drone attack failed "
                                           "to kill him.“I can buy what you bought.”Weapons smuggled from Florida are "
                                           "empowering the country’s militias and enabling them to challenge a "
                                           "fragile governmentIt was 5am on Tuesday, February 25 when members of Viv "
                                           "Ansanm, a coalition of Haiti’s gangs, announced their advance through the "
                                           "densely populated neighbourhood of Delmas 30 in the capital "
                                           "Port-au-Prince with bursts of\xa0gunfire.Wielding assault rifles, "
                                           "handguns and machetes, they looted homes and put them to the torch. Some "
                                           "people were burned alive in front of their children. Women were raped. "
                                           "Two off-duty soldiers, who were brothers, were killed in the "
                                           "onslaught.Among those who fled were Johnise Grisaule and her "
                                           "three-year-old son, who are now staying a few kilometres away in a clinic "
                                           "repurposed as a refugee camp, alongside more than 4,800 of their "
                                           "neighbours.“The police couldn’t do anything,” Grasaule says, on a recent "
                                           "sweltering afternoon, swatting away flies. “There were so many more "
                                           "bandits and with much bigger guns.”Haiti, the poorest country in the "
                                           "western hemisphere, is mired in a political, economic and security crisis "
                                           "that exploded with the assassination of President Jovenel Moïse in July "
                                           "2021. Gangs now control 90 per cent of metropolitan Port-au-Prince, "
                                           "according to the UN, encircling the transitional government’s last "
                                           "redoubt in the upscale suburb of Pétion-Ville.Services from healthcare "
                                           "and electricity to rubbish collection have collapsed, while gangs control "
                                           "the ports and all roads into the capital, extorting fees for goods that "
                                           "enter. Unable to flee, residents are crammed into safe\xa0zones.Countless "
                                           "neighbourhoods around the city, often deserted, show the aftermath of "
                                           "battle, with rubble lining the streets and bullet holes pockmarking the "
                                           "charred remains of buildings.“There is a real risk that Port-au-Prince "
                                           "will fall to the gangs, granting them political power across the country,"
                                           "” Haiti’s finance minister Alfred Métellus tells the\xa0FT.Outside the "
                                           "capital, gangs have continued their expansion. There were 5,626 murders "
                                           "recorded across Haiti last year, up 1,000 from 2023. The UN has reported "
                                           "a further 2,700 in the first five months of 2025. Around 1.3mn people, "
                                           "out of a population of 11.5mn, have been displaced, while 5.7mn people "
                                           "lack access to adequate\xa0food.Cumulative killings per yearFuelling the "
                                           "bloodshed is the gangs’ growing arsenal of military-style weaponry, "
                                           "much of which originates with purchases from US gun shops and ends in the "
                                           "slums of\xa0Haiti.“The problem is that in the USA, anyone can buy a "
                                           "weapon,” Metellus says. “Then they are shipped in [cargo] boxes from the "
                                           "Miami River.”The origins of Haiti’s gangs can be traced back to the 1960s "
                                           "and the feared Tonton Macoutes paramilitaries of the Duvalier "
                                           "dictatorships which lasted until\xa01986.Romain Le Cour Grandmaison, "
                                           "a researcher with the Global Initiative against Transnational Organized "
                                           "Crime, says the gangs grew out of militias formed by politicians and "
                                           "business owners wishing to rule areas informally and intimidate and "
                                           "disrupt their competitors, but that the money the groups made from "
                                           "extortion and smuggling gave them autonomy from their paymasters.The "
                                           "assassination of Moïse then created a power vacuum which they swiftly "
                                           "filled. The creation of Viv Ansanm at the start of 2024 — ending years of "
                                           "feuding between rival gangs — was a decisive turning point, "
                                           "say politicians and\xa0analysts.“It's a coalition of interest groups that "
                                           "has constructed the chaos that we are living through,” Fritz Jean, "
                                           "who chairs the transitional presidential council currently governing "
                                           "Haiti, tells the\xa0FT.Diego Da Rin, a Haiti analyst with the "
                                           "International Crisis Group, says that “there is a reason why the gangs "
                                           "started working together: to derail the security mission that could be "
                                           "stronger than them.”He adds that Viv Ansanm’s goal “is to reach the "
                                           "offices of the prime minister and the presidential council and topple the "
                                           "government, without offering a clear plan for what would follow.”The "
                                           "gangs’ metamorphosis into heavily-armed militias more akin to swat teams "
                                           "can be seen in the  videos they post of themselves on social\xa0media.In "
                                           "one slickly produced clip, the leader of the 5 Segonn gang, Johnson Andre "
                                           "— better known by his nom de guerre ‘Izo’ — flaunts weaponry and armour, "
                                           "which includes SUVs painted in camouflage colours and rifles fitted "
                                           "with\xa0scopes.In another post, Izo wears body armour and a ballistic "
                                           "helmet while taunting the Multinational Security Support Mission in Haiti "
                                           "(MSS) — a UN-approved and Kenyan-led force designed to bolster the "
                                           "country’s outmatched national\xa0police.The gangs are increasingly using "
                                           "these higher calibre weapons, says Robert Muggah, co-founder of the "
                                           "Igarapé Institute, a Brazil-based security thinktank that has been "
                                           "studying Haiti’s gangs. “Pistols and revolvers are one thing but an "
                                           "AR-15, or an M10, or a sniper rifle is another.”Muggah adds that even a "
                                           "relatively small number of guns — around 100 — “makes a massive "
                                           "difference in the calibration of force and the violence that can be "
                                           "generated”.An FT analysis of US court documents, shipping records and "
                                           "statements by Haitian and Dominican authorities shows how these guns are "
                                           "smuggled into the\xa0country.In February, the Sara Regina, a hulking 90m "
                                           "cargo ship, journeyed from Miami to Haina Occidental Port in the "
                                           "Dominican Republic — which shares the island of Hispaniola with Haiti — "
                                           "bringing with it a cache of\xa0weapons.The vessel was transporting a "
                                           "container with second-hand goods, including bicycles and refrigerators. "
                                           "Such items are frequently sent by Haitians in Florida to friends and "
                                           "relatives in their homeland, where even basic necessities are difficult "
                                           "to\xa0obtain.Hidden on the Sara Regina were nearly two dozen firearms and "
                                           "36,000 rounds of ammunition.The haul included boxes of cartridges made by "
                                           "Houston-based PMC Ammunition. The company’s slogan is, ‘America’s "
                                           "company. America’s ammunition’.Bullets manufactured by Fiocchi of America "
                                           "were also found. A video posted by a gang shows they already have large "
                                           "stocks of Fiocchi cartridges.Among the firearms were Glock pistols and 16 "
                                           "AK-type rifles, a weapon that often appears in gang videos.A UN report "
                                           "states that some were VSKA and WASR AK-variants. These are sold in the US "
                                           "by Century Arms. AK-type rifles are increasingly sought after by the "
                                           "gangs.Also in the haul was a US-manufactured Barrett M82, "
                                           "able to penetrate lightly armoured vehicles. A video shows a gang posing "
                                           "with another M82 and belts of .50 calibre rounds.The seizure by the "
                                           "Dominican customs officers showcases the firepower Haiti’s gangs are "
                                           "attempting to import from the US. Haiti does not manufacture firearms or "
                                           "bullets, with other guns wielded by the groups stolen from the Haitian "
                                           "military and\xa0police.In the first half of 2022, officials at Haina "
                                           "Occidental Port seized more than 112,000 “units of firearms and "
                                           "ammunition”, with much of it shipped from Miami, according to a "
                                           "UN\xa0report.Analysis of data from trade platform CargoFax reveals that "
                                           "between July 2020 and March 2023, 34 shipments were sent from US ports to "
                                           "Haitian individuals now on the US sanctions\xa0list.It included 24 "
                                           "shipments for Prophane Victor, a former member of parliament who has long "
                                           "been accused by the UN and US of arming gangs. The goods he received were "
                                           "described as personal effects — thrift store items and used\xa0shoes.Easy "
                                           "access to American weapons increases violence across the whole region, "
                                           "says Evan Ellis, professor of Latin American studies at the US Army War "
                                           "College. An October report by the US firearms enforcement agency says "
                                           "that 73 per cent of guns recovered in crimes in the Caribbean between "
                                           "2018-22 were from the US, mainly Florida, Georgia and Texas. Ellis adds "
                                           "that Haiti’s gangs also acquire body armour and other combat equipment "
                                           "from\xa0China.Miami has become the main hub for smuggling weapons to "
                                           "Haiti for a number of reasons: it has a large diaspora swelled by "
                                           "refugees; there is a loosely regulated export industry which sends small "
                                           "shipments to the country; and Florida’s lenient gun\xa0laws.Florida does "
                                           "not require a permit to purchase firearms and there is no limit on the "
                                           "number that can be bought in a single transaction. In 2023, "
                                           "Florida scrapped the mandatory training, licensing fees and background "
                                           "checks required to carry a concealed weapon. There are also few "
                                           "restrictions on buying ammunition.“It's a huge issue,” says Sheila "
                                           "Cherfilus-McCormick, a congresswoman representing South Florida in the "
                                           "House of Representatives and the only sitting Haitian-American lawmaker. "
                                           "“Maybe 80 to 85 per cent of the guns in Haiti come from the US — and "
                                           "they’re directly coming from the Miami River.” She adds that with Florida "
                                           "regulations making it even easier to buy guns, anybody “in cahoots” with "
                                           "the gangs is able to purchase weapons and send them to\xa0Haiti.“Lax US "
                                           "gun laws allow gangs to source military grade weaponry almost freely,"
                                           "” says Louis-Henri Mars, executive director of Lakou Lapè, "
                                           "a Port-au-Prince-based peace-building organisation.Joseph Lestrange, "
                                           "a former senior official investigating transnational organised crime at "
                                           "the US Department of Homeland Security (DHS), says that the purchases "
                                           "begin with the gangs finding people who are eligible to buy them on "
                                           "behalf of those who are\xa0not.“You have transnational criminal "
                                           "organisations who pay recruiters to find straw buyers with clean criminal "
                                           "records”, Lestrange says. They can then “easily go into a federal "
                                           "firearms license dealer and buy one, two or a few firearms, depending on "
                                           "the laws that apply to that state.”Analysis of US court records from an "
                                           "earlier arms seizure sheds light on how this process\xa0works.I should "
                                           "buy about 3 guns like this. They are big guns, baby, big guns . . . "
                                           "That's something I can use to do a lot of bad things . . . you can wipe "
                                           "out an area completely.In 2021, Joly Germine, a leader of 400 Mawozo, "
                                           "one of Haiti’s largest gangs, organised the purchase of guns from his "
                                           "jail cell in Haiti. Court documents state that Germine used WhatsApp to "
                                           "instruct Florida-based straw buyers to obtain military-style rifles — "
                                           "weapons he said would give him dominance over the Haitian police and "
                                           "enable him to inflict huge casualties.I should buy about 3 guns like "
                                           "this. They are big guns, baby, big guns . . . That's something I can use "
                                           "to do a lot of bad things . . . you can wipe out an area completely.The "
                                           "stuff is heavy. He [the shipper] complained . . . He hasn’t complained "
                                           "about the one I prepared today, but the other two drums, "
                                           "a lot of trouble.From March to November, two Florida-based Haitians "
                                           "bought 24 weapons from gun shops in the state, including a Barrett M82 "
                                           ".50 calibre anti-materiel rifle and 9 Century Arms AK-type rifles, "
                                           "court documents show. Assisted by Germine’s girlfriend, Eliande Tunis, "
                                           "the group planned to hide the guns in barrels and transport them to "
                                           "Haiti. The conspirators completed two weapons shipments, with a third "
                                           "seized in an FBI raid on a lock up in\xa0Orlando.The stuff is heavy. He ["
                                           "the shipper] complained . . . He hasn’t complained about the one I "
                                           "prepared today, but the other two drums, a lot of trouble.The money to "
                                           "buy the guns had come from a series of kidnappings carried out in Haiti "
                                           "by 400 Mawozo, prosecutors say. In June and July 2021, $25,000 was paid "
                                           "to the gang to secure the release of two US citizens, with $50,"
                                           "000 paid to free a third American hostage the next\xa0month.The gang "
                                           "often used money transfer services, breaking large amounts down into "
                                           "smaller transactions and using multiple services on the same day to avoid "
                                           "suspicion. In this way, the gang sent $37,500 to the US between March and "
                                           "October\xa02021.Germine, who was extradited to the US in 2022, "
                                           "pleaded guilty to the gun trafficking charges in 2024 and was found "
                                           "guilty in May for his involvement in the hostage taking of American "
                                           "citizens in\xa0Haiti.One of the shops used by Germine’s straw buyers was "
                                           "Lucky Pawn, a small pawnbroker that sits on the side of a highway in the "
                                           "north of Miami and purchases and sells cars, jewellery and\xa0guns.When "
                                           "approached by the FT, an employee named Frankie, the store’s jeweller, "
                                           "declined to provide details on what checks are carried out on customers, "
                                           "dismissing the volume of guns shipped from Florida to Haiti as "
                                           "insignificant compared to US military support for Israel. “This is shit "
                                           "compared to what’s being sent to Gaza, paid for by American taxpayers,"
                                           "” said Frankie, who declined to give a\xa0surname.Once the weapons have "
                                           "been purchased, freight forwarders — companies that consolidate and "
                                           "package shipments into container loads — are the next step in the illicit "
                                           "supply\xa0chain.The container aboard the Sara Regina, the ship which was "
                                           "seized in February in the Dominican Republic, originated with a freight "
                                           "forwarding group called Eugenio Trading, located in a non-descript Miami "
                                           "warehouse in an industrial district north of the city’s airport. The "
                                           "group specialises in sending clothing to the Caribbean.The company’s "
                                           "owner, Urbano Eugenio Garcia, is now in pre-trial detention in Santo "
                                           "Domingo in connection with the seizure of the vessel. But his son Sergio "
                                           "says his father was “used” by gun smugglers after a Haitian woman "
                                           "approached him last year to send an empty container to Jacksonville for a "
                                           "supposed furniture shipment to\xa0Haiti.“We don’t usually do this for "
                                           "anybody,” Eugenio Jnr told the FT. “We did it as a favour . . . we were "
                                           "used.”But Eugenio Jnr says there is little that can be done by freight "
                                           "forwarding companies like his to prevent such shipments given the scale "
                                           "of the operations. “The weapons are so micro compared to a container,"
                                           "” he says. “I cannot go and sit and watch them load the container all "
                                           "day.”In a report published last year on the escalating violence in Haiti, "
                                           "the UN Security Council provided another example of freight forwarders "
                                           "being used by smugglers.In this case, a container was filled with boxes "
                                           "of household goods from more than 100 individuals. Hidden in two of them "
                                           "were 26 firearms as well as ammunition. One box was collected by a port "
                                           "customs officer who was later arrested and removed from "
                                           "his\xa0position.The freight forwarder denied being involved in the "
                                           "smuggling and told the UN that typically clients hand over goods that are "
                                           "already packaged and sealed. He went on to say that the client —\xa0who "
                                           "paid $150 for the delivery —\xa0had provided a copy of his ID via "
                                           "WhatsApp, and deleted the message shortly afterwards. The UN report added "
                                           "that the shipping company was unlikely to be aware it was transporting "
                                           "illicit\xa0firearms.For law enforcement trying to enforce export "
                                           "regulations, a lack of resources is a core part of the problem, "
                                           "says Lestrange, the former DHS official. He adds that US Customs and "
                                           "Border Protection agents checked less than 5 per cent of exports when he "
                                           "left DHS three years ago. In the majority of cases, paperwork isn’t "
                                           "required for exports valued at $2,500 or less, further reducing "
                                           "oversight.From the freight forwarders, the cargo is transferred to "
                                           "carriers who transport the goods to Haiti. Three miles from Eugenio "
                                           "Trading’s warehouse, on the Miami River, is Antillean Marine, the largest "
                                           "shipping carrier for cargo travelling between Miami and Haiti and the "
                                           "group that operates the Sara Regina. The company declined to speak to the "
                                           "FT about the cache of guns on the\xa0vessel.The danger posed by gangs at "
                                           "Haiti’s ports means shipments to the country increasingly arrive via the "
                                           "Dominican Republic, with goods then driven across the\xa0border.The "
                                           "weapons seized on the Sara Regina were meant to take this route. Shipping "
                                           "records show they were to be received in Haina Occidental Port by a man "
                                           "based in the Dominican border town of Elias Pina, before being "
                                           "transported to the Haitian town of Belladere.The 400 Mawozo gang are "
                                           "active in the area and control the road that connects Belladere to "
                                           "Port-au-Prince, making the gang or one of its allies the potential "
                                           "recipients.400 Mawozo are adept at acquiring arms, says security expert "
                                           "Muggah, which they sell on to other gangs. The fact that several of their "
                                           "members have served time in US prisons has enabled them to develop the "
                                           "skills and network needed to procure these weapons, Muggah\xa0adds.While "
                                           "handguns might go for $400-500 at federally-licensed firearms outlets in "
                                           "the US, they can command as much as $10,000 in Haiti. Prices go up for "
                                           "sought-after, high-velocity weapons such as AKs, AR-15s and Galil rifles. "
                                           "A Barrett M82 could sell for $22,000, according to the\xa0UN.Métellus, "
                                           "the Haitian Finance Minister, says the country plans to step up checks at "
                                           "its land border with the Dominican Republic in an attempt to reduce the "
                                           "gangs’ revenue\xa0streams.Gangs on the Haitian side of the border charge "
                                           "$2,000 for each container that passes through, Métellus says. With 5,"
                                           "000 containers crossing the border a month, the trade could be worth "
                                           "$120mn a year. The government, meanwhile, is losing $3.8million per day "
                                           "in customs duties from the now gang-controlled port in the capital, "
                                           "Port-au-Prince.“The national police is not well-equipped,” Métellus says. "
                                           "“Their budget annually is around $51m, so you see the challenge. The "
                                           "strategy is to block the flow of money.”Efforts to stem the flow of "
                                           "weapons — including a UN-imposed arms embargo in October 2022 and the US "
                                           "declaration of  Viv Ansamn as a foreign terrorist organisation — have so "
                                           "far failed to yield results in Haiti, where the security crisis continues "
                                           "to\xa0worsen.On the ground, MSS, the Kenyan-led security mission, "
                                           "has made little gains since it arrived in June last year. In a desperate "
                                           "bid to change the tide of battle, Haiti’s presidential council has turned "
                                           "to employing US mercenaries and attacking the gangs with explosive-laden "
                                           "“kamikaze” drones, like the one sent in March, unsuccessfully, "
                                           "to kill Cherizier, head of the Viv Ansanm\xa0alliance.Your browser "
                                           "doesn't support HTML5 video.Your browser doesn't support HTML5 video.“The "
                                           "Haitian government cannot now tackle the gangs without international "
                                           "support, and I’m not talking about the farce of the MSS,” says James "
                                           "Boyard, a security analyst based in the\xa0capital.At the end of May, "
                                           "Haitian media reported that the leader of the 5 Segonn gang had been "
                                           "seriously injured and several members killed in a drone attack. At least "
                                           "345 gang members have died following drone strikes since March, "
                                           "data from conflict monitoring group Acled\xa0shows.In contested "
                                           "neighbourhoods, local resistance fighters and vigilante groups engage the "
                                           "gangs in shootouts using guns believed by humanitarian workers to also be "
                                           "supplied by Haiti’s US-based diaspora. Gang members now avoid exposing "
                                           "their positions in the open streets and are increasingly fighting "
                                           "house-to-house, blasting through walls as they\xa0go.“It’s all about "
                                           "staying alert, and closely monitoring the gangs’ movements,” says one "
                                           "resident. “The self-defence force works in close communication with the "
                                           "police, and on operations they are there guiding them.”In the political "
                                           "sphere, the transitional presidential council — installed after the "
                                           "collapse of the government of Moïse’s successor Ariel Henry in April 2024 "
                                           "— has been wracked with infighting and corruption allegations, "
                                           "and is unlikely to convene Haiti’s first elections since 2016 before its "
                                           "mandate expires in February. If elections are held, observers worry yet "
                                           "more violence could\xa0flare.“When you do this, you have an immense "
                                           "number of extremely [well] armed and violent actors that will start "
                                           "bargaining again for political power, for political favors, for seats, "
                                           "for allies,” says researcher Le Cour Grandmaison.At the refugee camp in "
                                           "Port-au-Prince — one of more than 200 nationwide and 80 in the capital — "
                                           "the humanitarian consequences of the gangs’ onslaught "
                                           "are\xa0clear.Children miss meals and latrines overflow. Some residents "
                                           "have set up charcoal stoves indoors, the smoke billowing around the "
                                           "stuffy, unventilated living space. Health workers have documented cases "
                                           "of cholera and tuberculosis.“There is no chance for Haiti without "
                                           "security,” says Medelaine Ernst, who is living in the camp with her three "
                                           "young children after fleeing the Delmas 30 neighborhood. “Things will "
                                           "only get worse for us.”Leonard Fritz, a community leader in the camp, "
                                           "estimates that tens of people lost their lives in the massacre from which "
                                           "he ran. “It was chaos and panic,” he says, raising his voice above the "
                                           "whirring from an aid helicopter flying\xa0overhead.Volker Türk, "
                                           "the UN High Commissioner for Human Rights, said in June that the "
                                           "“crucial” coming months will “test the international community’s ability "
                                           "to take stronger, more coordinated action” to determine the country’s "
                                           "future stability.“No more illegal weapons should be allowed to facilitate "
                                           "the horrors unfolding in Haiti.”Additional research by Casper Baehr, "
                                           "Lars Brull, Alix Convent, Constanza Mottin and Ronan Verbeek of Utrecht "
                                           "University Open-Source Global Justice Investigations\xa0Lab.",
                                'word_count': 3680,
                                'author': '',
                                'tags': [],
                                'related_articles': []
                                }
list_article_pub_date = '2025-08-03 14:00:04.653000+03:00'
list_article_link_and_title = ('/content/040a6816-4fc6-4014-bb26-45c9e814de9b',
                               'The brave new world of trade has arrived ')
list_article_subtitle = 'Donald Trump has reset the global trading order. What happens next?'
first_list_article_preliminary_information = {
                                              'published_at': datetime.datetime(2025, 8, 3, 21, 19, 58,
                                                                                tzinfo=zoneinfo.ZoneInfo(key='Europe/Kyiv')),
                                              'url': '/content/90e2efe6-28de-427e-ad95-e3a62cbdd85a',
                                              'title': 'Motor finance redress scheme to cost banks up to £18bn, says FCA',
                                              'image_url': None,
                                              'subtitle': 'Financial watchdog to give detailed proposals in October, '
                                                          'following Friday’s Supreme Court ruling '
                                              }



