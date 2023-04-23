from selenium.webdriver.common.by import By

class FramesPO():
    heading = (By.CSS_SELECTOR,".example h3")
    nestedFrames = (By.LINK_TEXT,"Nested Frames")
    iframelink = (By.LINK_TEXT,"iFrame")
    leftFrameText = (By.CSS_SELECTOR,"body")
    middleFrameText = (By.ID,"content")
    bottomFrameText = (By.CSS_SELECTOR,"body")
    topFrame = (By.NAME,"frame-top")
    leftFrame = (By.NAME,"frame-left")
    middleFrame = (By.NAME,"frame-middle")
    bottomFrame = (By.NAME,"frame-bottom")
    iFrame = (By.ID,"mce_0_ifr")
    iframeText = (By.CSS_SELECTOR,"#tinymce p")


