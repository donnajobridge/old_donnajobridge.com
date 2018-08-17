Title: memory is malleable
Slug: update
Date: 2018-07-25
Tags: memory, updating, false memory, cognitive neuroscience, data science
Image: /images/update_icon.jpg

Do you have a friend who tells the same story at every party? Have you noticed how on each iteration the sky gets darker, the water gets deeper, and the guppy slowly morphs into a whale? Does this mean your friend is a big fat liar? Well maybe a little. But, this is also a natural feature of our memory. It turns out our memories are not static representations of past events like a photo or a video recording, but they dynamically change every time you think about them.

It may seem troublesome that we don’t keep accurate representations of the past stored in our memories -- but I would argue that this is actually an adaptive process that allows us to cope with our constantly-changing situations. For instance, if our memories stayed the same and never changed, you would never learn that your partner is now 20 years older than when you met him, because the younger version of him would prevail in your memory — it would never get updated with constantly changing information (gray hair, wrinkles around the eyes, etc.).

![fig1](/images/telephone_fishing.png)

###what happens to our memories over time?
Remember the Telephone Game? The first person whispers “My new blue shoes”. After a few whispers down the line, the final person hears “I know voodoo”. Each person hears something a little different, because they only hear a distorted version of the original due to low-quality signal. In the telephone game, some words drop out entirely from the message, other words get changed to new words, and completely new words somehow get inserted out of thin air. Our memories behave similarly. In the telephone game, one message is passed from one person to another. But with memory, the message is passed from our past self to our current self every time we remember it. And this happens over and over again each time we remember an experience.

Contrast this idea with how people usually think about memory: as some unchanging photograph. In this view, when you remember an event and take out your “original” or “master copy” of the photograph, and look at it. You might notice different things, but it’s still the same, unchanging photo. The “telephone game” theory of memory on the other hand has no “master copy”, it just has a message that is continuously altered every time you think about it.

This feels a little weird. Why wouldn’t we notice our memories changing? It’s because we only experienced the event once, but we recall it many times. Unfortunately, unless we had a video recording of the entire event (and a view from our first person perspective), we can’t compare our current version to the original. We only have the last time we remembered it fresh in our memories. Because of that, we can be highly confident that we are accurately remembering an event, when in fact, we are recalling *the last time we remembered* the original event.

Our memories can change in a few different ways. First, the most common complaint about memory is that we forget details (and sometimes entire events). What was his name? What color dress was she wearing? Second, we don’t just forget, but we *fill in* pieces of the story with information that *was not from the original experience*. The filler information is often something we've encountered, just not during the original event. This is like two different experiences crossing over into one memory. It might seem relatively inconsequential to forget some details or for some details to morph into others, but it’s disconcerting how this type of information is relied heavily on in a courtroom when there is an eye witness.

###measuring memory change
Most memory studies rely on showing someone a stimuli (like a word or photograph), waiting, and then asking if the person remembered that thing. The yields a simple “yes” or “no” response -- there is no gray area. It’s difficult to measure *how much* a memory changed in this type of test format. To get around this problem, I designed a spatial memory task that required subjects to use the mouse to place an object back in its location. This type of task yielded a graded measure of memory: distance. I was able to measure the distance each object was placed from the original location and track how placement changed over the course of multiple tests.

I designed the experiment to examine how a memory shifts each time we remember it. In this study, participants learned object-location associations, meaning each object was presented in a specific location on the screen. I tested the subjects every day for three days. subjects were asked to place each object back in its original location. As in real life after we experience an event, subjects never received feedback about whether or not they had placed the object in the correct spot. With this test, I was able to measure the two features of memory distortion: 1) How much did participants forget the original location of the course of the three days? and 2) Did the locations they chose depend more on the *original location* or on the *location that they had last selected*?

![fig2](/images/telephone_spatial.jpg)

First I looked at *forgetting* by seeing how far away they placed the object over the three-day period. For this analysis, I simply measured the distance each object was placed from its original location on each of the tests at Day 1, Day 2, and Day 3. Interestingly, there was a big drop in performance from Day 1 to Day 2, but forgetting leveled off, as memory declined substantially less from Day 2 to Day 3. These results suggest that after an event, our memory drops off immediately, and we forget a lot of the details and context information. But after that initial drop-off period, our memories maintain stability. These results are in line with other studies of memory consolidation that show that older memories are more stable than newer memories. It also resembles the classic [Ebbinghause forgetting curve](https://en.wikipedia.org/wiki/Forgetting_curve), which shows a steep drop-off in accuracy immediately after learning and then levels off as time goes on.

![fig3](/images/react_kdeForgetting.png)

Next I looked at how each test influenced the content of memory on each subsequent test. For this analysis, I looked at final memory outcome on the Day 3 test. I measured the distance each object was placed from 3 different locations: the originally studied location, the location subjects placed the object on the Day 1 test, and the location subjects placed the object on the Day 2 test. In this way, I could see how each of these experiences influenced where subjects placed the object on the final Day 3 test. Interestingly, the results showed increasing influence of the most recent test on final memory performance. Subjects placed objects closest to the Day 2 test location, followed by the Day 1 test location, and farthest from the originally studied location. [(Bridge, 2012)](/pdfs/bridge12.pdf)

![fig4](/images/react_kdeUpdating.png)

These results show the powerful influence each experience of remembering has on our final memory. Each time we remember an event, information from that experience of remembering gets incorporated into the original memory, causing it to change slightly each time. This type of study makes you wonder what a memory actually is. How much is it really reliving the original experience? It seems that our memories are more colored by each experience we have of reminiscing about those old times. Our memories change with us, and reflect more about who we currently are rather than who we were.

###it’s not just about what you experienced recently…
Based on that study, it could be that case that every time we remember an event, we change it by incorporating the retrieved information into the original memory. But, there is an alternative hypothesis. It could be, that we are just more likely to remember things that happened recently rather than things that happened far in the past. Subjects remembered the Day 2 test location the best on the Day 3 test, but they also encountered that location most recently. To get to the bottom of this, I designed another study to determine if recency was really the underlying cause of this effect.

In this new study, I implemented 2 different conditions. First, subjects studied objects in unique locations. Then, in an “Active” condition, I asked subjects to place each object back in its original location (to the best of their ability), so they were required to remember each object’s location as in the first study. In a second condition called a “Passive” condition, I randomly chose new locations on the screen and told subjects to place each object in one of these random locations. So to clarify the differences in these conditions, in the Active condition, subjects had to recall from memory each object’s location (which always diverged a bit from the original location, because our memory is never perfect!). On the other hand, in the Passive condition, I chose the wrong locations for subjects to place each object in. After the Active or Passive manipulation, subjects completed a final test. On this test, they saw each object in 3 locations, and they were prompted to select the object’s original location. The object choices were the original location, the updated location, and a new location.

![fig5](/images/cxtupDesign_samecxt.jpg)

If the updating effect I saw in the first study was really just about recency, it shouldn’t matter if I show subjects the wrong location or that mistakenly recall the wrong location -- they should remember the most recently encountered location on the final test. On the other hand, if updating only happens when we actively remember the wrong location, then subjects should only choose the updated location in the Active condition, but not the Passive condition.

###results
It turns out remembering events is really special. Subjects were not easily tricked into thinking the wrong location I selected was the object’s original location. In the Passive location, subjects disproportionately chose the original location over the other options. However, updating was prevalent in the Active condition. Subjects usually chose the updated (incorrectly remembered) location on the final test instead of the other choices. These results show that remembering events provides an opportunity to update them. The good news is that we are not easily fooled by incorrect information that does not match our memories. [(Bridge, 2014 (1))](/pdfs/bridge14jon.pdf)

<p align='center'>
<img src="/images/cxtup_swarm.png" alt="fig6" style="width:75%;"/>
</p>

###where does this study fall on the consciousness continuum?
These studies involved explicit responses from participants. On each test, I explicitly asked participants to place the objects back in their original locations. On the final test, they tended to erroneously remember the previously remembered location rather than the original location. I would argue that the process of memory updating was unconscious. Subjects were not aware that their memory changed each time I tested them. These studies goes to show that even when we do some explicit actions (intentionally remembering an event), new information can seep into those memories due to unconscious processes happening in our brain.

###main points
* There’s no true unadulterated original version memory stored in your brain, unless it was never accessed (remembered). But if that were the case, it would probably be buried or forgotten.
* Our memories are engineered to change. This is adaptive, and helps us learn new information quickly and efficiently. [(Bridge, 2014 (2))](/pdfs/bridge14nsy.pdf)

###press links
* [npr](https://www.npr.org/sections/health-shots/2014/02/04/271527934/our-brains-rewrite-our-memories-putting-present-in-the-past)
* [la times](http://www.latimes.com/science/sciencenow/la-sci-sn-memory-updating-20140204-story.html#axzz2sSngvyz8)
* [wgn](https://wgntv.com/2014/02/04/study-minds-incorporate-new-information-into-original-memories/)
* [wttw](https://chicagotonight.wttw.com/2012/10/31/distorted-memories)
* [cnn](http://thechart.blogs.cnn.com/2012/09/20/your-memory-is-like-a-game-of-telephone/)


###data & analysis
* [experiment 1](https://github.com/donnajobridge/data_visualizations/tree/master/react)
* [experiment 2](https://github.com/donnajobridge/data_visualizations/tree/master/cxtupdate)
