## All setting and transition goes into this file

image ev showdown = "event/lilly_shizu_showdown.jpg"
image ev showdown_large = "event/lilly_shizu_showdown_large.jpg"
image ev showdown_lilly = im.Crop("event/lilly_shizu_showdown_large.jpg", 280*2.4,100*2.4,1920,1080)
image ev showdown_shizu = im.Crop("event/lilly_shizu_showdown_large.jpg", 1400*2.4,160*2.4,1920,1080)

image showdown_lilly_slice = im.Crop("event/lilly_shizu_showdown_large.jpg", 440*2.4,260*2.4,1920,1080/2)
image showdown_shizu_slice = im.Crop("event/lilly_shizu_showdown_large.jpg", 1360*2.4,320*2.4,1920,1080/2)
image showdown_lilly_full_slice = im.Crop("event/lilly_shizu_showdown_large.jpg", 280*2.4,100*2.4, 1920*1.15,1080*1.15)
image showdown_shizu_full_slice = im.Crop("event/lilly_shizu_showdown_large.jpg", 1360*2.4,320*2.4,1920,1080)

image fw_blank = Solid("#00000000")
image fw_flash = Solid("#2b2b2b66")
image darkgrey = Solid("#0D0D0D")
image soft = Solid("#F5D4A1")

transform twoleft:
        xpos 300
        yalign 1.0
        ypos 1.0
    
transform tworight:
        yalign 1.0
        xpos 1100
        ypos 1.0

transform threeleft:
        xpos 100
        yalign 1.0
        ypos 1.0
    
transform threeright:
        yalign 1.0
        xpos 1300
        ypos 1.0

define flash = Fade(.25, 0, .75, color="#fff")

define openeye = ImageDissolve("vfx/tr_eyes.png", 1.0, 64, ramptype="cube")
define shuteye = ImageDissolve("vfx/tr_eyes.png", 1.0, 64, ramptype="mcube", reverse=True)


define fw_dis_fast = Dissolve(0.04, alpha=True)
define fw_dis_medium = Dissolve(0.2, alpha=True)
define fw_dis_slow = Dissolve(3.0, alpha=True)
define fw_sparkle_out = ImageDissolve(im.Tile("vfx/tr-pronoise.png"), 3.0, 32, alpha=True)

transform fw_constructor(my_image):
    "fw_blank" 
    choice 15:
        0.2 
    choice:
        "fw_flash"  with fw_dis_fast 
        0.2 
        choice:
            my_image  with fw_dis_medium 
            "fw_blank"  with fw_dis_slow 
            6.0 
        choice:
            my_image  with fw_dis_medium 
            "fw_blank"  with fw_sparkle_out 
            6.0 
    repeat



image fireworks = LiveComposite((1920, 1080),
(0,0), fw_constructor("vfx/fw1.png"),
(0,0), fw_constructor("vfx/fw2.png"),
(0,0), fw_constructor("vfx/fw3.png"),
(0,0), fw_constructor("vfx/fw4.png"),
(0,0), fw_constructor("vfx/fw5.png"),
(0,0), fw_constructor("vfx/fw6.png"),
(0,0), fw_constructor("vfx/fw7.png"),
(0,0), fw_constructor("vfx/fw8.png"),
(0,0), fw_constructor("vfx/fw9.png"))

transform fw_constructor_nosparkle(my_image):
    "fw_blank" 
    choice 15:
        0.2 
    choice:
        "fw_flash"  with fw_dis_fast 
        0.2 
        my_image  with fw_dis_medium 
        "fw_blank"  with fw_dis_slow 
        6.0 
    repeat


define sfx_fireworks = "sfx/fireworks.ogg"