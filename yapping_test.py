from yapper import Yapper, PiperSpeaker, PiperVoiceUS, PiperQuality

lessac = PiperSpeaker(
    voice=PiperVoiceUS.RYAN
)
lessac.say("hello")

yapper = Yapper(speaker=lessac)
yapper.yap("<some random text>")
yapper.yap("Tonight, we find ourselves in a small, quiet town, nestled away from the hustle and bustle of city life. But beneath the calm surface, something sinister is brewing. A dangerous Mafia family has infiltrated the town, and they’ll stop at nothing to take control. The townspeople are in a race against time to unmask the Mafia before it's too late. You, my friends, are caught in the middle of this intense battle. Some of you are the innocent townsfolk, trying to root out the Mafias deceitful ways. Some of you are the Mafia, blending in and trying to manipulate the crowd to carry out your sinister plan. And a few of you might have special powers, with roles to uncover the truth or protect the innocent. Tonight, trust is in short supply, and only your wits will determine who survives. So, keep your eyes sharp, your words sharp, and your secrets even sharper. The Mafia is among you... and only one side can emerge victorious!")