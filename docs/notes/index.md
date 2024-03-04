# Notes

# Protection/Signatures

So, it seems that `hanime` does indeed have protection on some of the more serious endpoints, including the comments, etc. It's just a signature, `x-signature`, and it doesn't seem to be hard to reverse.

I will look into it more in my free time. Besides that, they use Google reCAPTCHA for some other endpoints, not any you'd really need, mostly just for actions like registration and login. For future cases where I plan to add any functions that require the user to be logged in, I will incorporate some way to navigate through this.

Google reCAPTCHA itself isn't the safest captcha; there are many ways to solve it, including browser-based solvers. I don't even need to do much; I can most likely use a headless `playwright` and proceed based on that. Well, I'll see. Just for an alternative and faster method, I would add support for captcha-solving services such as `capmonster`.

# Motive
I had no specific motive behind this; it was mostly borne out of boredom. When I first "made" this, it was around November 2023, in the first week of November, at around 2 in the morning. I had a poorly structured code since I never tried to make it good and kind of just left it as is.

I stumbled upon it deep in my projects and decided to bring it back to life. Anyway, who knows how this project will go. Probably not great, but let's be optimistic. So, I redid the code and made it WAY better. If you saw the previous code, yikes, it was horrible.