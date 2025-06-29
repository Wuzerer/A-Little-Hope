image splash_bg = "gui/logo_bg.png"
image splash_logo = "gui/logo.png"
image disclamer1 = "gui/disclamer1.png"

label splashscreen:
    scene splash_bg with dissolve
    show splash_logo at transform_splash_red_lolly
    $renpy.pause(2)
    $renpy.pause(1, hard=True)

    scene disclamer1 with Fade(1,0,1)
    $renpy.pause(3)
    $renpy.pause(1, hard=True)

    scene black with Fade(1,0,0)
    
    return

transform transform_splash_red_lolly:
    align (0.5, 0.5)
    zoom 0.25
    alpha 0.0
    block:
        parallel:
            ease 1.5 zoom 1.0
        parallel:
            ease 1.0 alpha 1.0
