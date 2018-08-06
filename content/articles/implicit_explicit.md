Title: consciousness continuum
Slug: continuum
Date: 2018-07-22
Tags: memory, explicit, implicit, cognitive neuroscience, data science
Image: /images/continuum_big.jpg

One reason that human behavior is so complex is that it can arise from unconscious and conscious sources. A simple example is breathing -- breathing is done automatically, we don’t have to consciously think about inhaling and exhaling every couple of seconds. That would be an extremely inefficient use of our limited cognitive resources! However, if you’ve ever done yoga or meditation, you are well aware that you can take control of your breathing. You can elongate your inhales, or breath quickly and rhythmically just by commanding your attention to your breath. This combination of conscious and unconscious processing that gives rise to our behavior is an area of intense research. Even researchers who study exclusively conscious (or explicit) cognitive processes (as I do), have to contend with influences of unconscious (or implicit) processing.

My area of research has focused on human learning and memory. I use a variety of methods to measure conscious and unconscious processing to understand how they interact to give rise to our experience of learning and remembering. The methods I use measure different levels of conscious processing. Combining them provides a complex picture of how our brains operate to guide our behavior.

###neural processing
At the bottom of the consciousness continuum is neural processing. Our brain is working nonstop behind the scenes, and we don’t have much knowledge about what it’s doing and when it’s doing it. Given the rapid processing speed of our brains, it’s not surprising we can’t keep up with it. I measure brain activity using a number of different techniques to determine how our brain processes information. One technique is called fMRI, which measures blood flow. When we use a part of our brain in a certain task, oxygenated blood flows to that region. However, blood flow changes (10-15 seconds) are very slow compared to brain activity (tens of milliseconds), so we can't get precise timing about when the brain responds to a stimulus. The main advantage of this technique is that we can get great spatial resolution about where the activity happens.

<div class="clearfix">
<div class="column icon_big">
<h4> fMRI activity related to memory</h4>
</div>
</div>

<div class="clearfix">
<div class="column icon_big">
<img class="icon" src='/images/bold.png'>
</div>
<div class="column icon_title_big">
<img src='/images/eeg.png'>
</div>
</div>

Another technique I use for studying brain activity is called EEG (electrocorticography), which measures electrical activity from the brain. We can decompose this raw electrical activity into distinct frequency bands by applying the Fourier Transform to the timeseries data. The primary benefit of this technique is that it has highly precise temporal resolution -- we can detect changes in electrical activity on the millisecond time scale. This technique comes in a couple forms, and I've used two of them. The most common form is scalp EEG, which measures electrical activity emanating from the scalp. However, a really exciting (and rare) form of of this technique is called intracranial EEG. This technique records electrical activity directly from the brain -- the electrodes are implanted deep into the brain rather than lying on the outer scalp. To do this research, I work with epilepsy patients who have these electrodes implanted for clinical purposes. This technique has the best of both worlds, high spatial resolution and high temporal resolution. The downside is that patients are very rare and their brains may be slightly abnormal due to epilepsy.

###eye movements
Next up on the continuum is eye movements. Eye movements occur rapidly -- we make 3 to 5 distinct eye movements per second. You are only consciously aware of only a subset of the eye movements you make. This is because different processes (e.g. perception, attention, and memory) can dictate what you look at and when, before you have the chance to make a conscious decision about where to look.

For example, imagine a small child did something wrong -- he broke the cookie jar. To cover up his mistake, he crudely hid it behind a chair. You ask, what happened to the cookie jar? He doesn’t answer, but you know immediately by his gaze where the cookie jar remnants are. The child doesn’t want to give away that information, but his eyes couldn’t help but look at the evidence.

![fig2](/images/cookie.png)

Of course we also move our eyes deliberately to certain locations, for instance when we are trying to pay attention to someone talking or when we are searching the room for our keys. The main point is that eye movements can be governed by both conscious and unconscious forces. They can provide rich information about what a person might be thinking on a rapid time scale by revealing the evolution of our thoughts . In the [eyes are the window to the brain section](eyes.html), I talk more about eye movements and how I've used them to deepen our understanding of the brain and human behavior.

###behavior
The next step in the continuum is behavior. The specific type of behavior I’m talking about is what cognitive neuroscientists typically measure to link cognition (or thinking) to neural activity. For instance, in a standard memory task, subjects view 100 images of various objects. After a delay, subjects are shown 200 images -- a mixture of images they saw before and images they have never seen. When the subject sees an image on the test, they make a button press indicating if they remember it or not.

This type of behavioral response gives reasonably good information about the content of people’s memory. However, it is lacking in a few ways. For instance, when the subject first sees the image, he may first scan the picture to find any features that were familiar. Then, he searched his memory for any matches. Maybe he finds it is a partial match. He then makes a decision about how confident he is that he did indeed see that exact image before. And finally, he plans the motor response to initiate the movement of his finger to press the appropriate button.

When we simply measure the final response, we are unable to capture that dynamic processing that led up to the ultimate behavior. Nonetheless, it does provide some useful information, and it is prevalently used in the field.

###feedback
The final step in the continuum is feedback. Primarily, I’ve used feedback from participants when I’m trying out a new experiment and working out the kinks. After they complete a task, I’ll sit down with the participants and ask them their thoughts on the task. What strategy did they use? Did it feel too hard? Was there anything peculiar about the stimuli? Getting direct feedback from the participants saves a lot of time when I’m designing new experiments. You don’t want to end up with an experiment with some glaring errors that were readily detected by the participants. Also, people are pretty perceptive, so it’s useful to take advantage of their thoughts to improve your design.
