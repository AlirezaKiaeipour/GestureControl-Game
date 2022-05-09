import cv2
import mediapipe as mp

mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpdraw = mp.solutions.drawing_utils
Draw_spec = mpdraw.DrawingSpec(thickness=2,circle_radius=2,color=(0,255,0))
cap = cv2.VideoCapture(0)

class Hand:
    def __init__(self):
        self.finger = []
        _,frame = cap.read()
        h,w = frame.shape[:2]
        frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                for index,lm in enumerate(hand.landmark):
                    x,y = int(lm.x*w),int(lm.y*h)
                    self.finger.append([index,x,y])
                mpdraw.draw_landmarks(frame,hand,mpHand.HAND_CONNECTIONS,Draw_spec,Draw_spec)
        cv2.imshow("Snake Game",frame)

    def gesture(self):
        try:
            if self.finger[8][2] < self.finger[5][2] and not self.finger[12][2] < self.finger[9][2] and \
                not self.finger[16][2] < self.finger[13][2] and not self.finger[20][2] < self.finger[17][2]:
                return "right"
            
            if self.finger[8][2] < self.finger[5][2] and self.finger[12][2] < self.finger[9][2] and \
                not self.finger[16][2] < self.finger[13][2] and not self.finger[20][2] < self.finger[17][2]:
                return "left"

            if self.finger[8][2] < self.finger[5][2] and self.finger[12][2] < self.finger[9][2] and \
            self.finger[16][2] < self.finger[13][2] and not self.finger[20][2] < self.finger[17][2]:
                return "up"

            if self.finger[8][2] < self.finger[5][2] and self.finger[12][2] < self.finger[9][2] and \
            self.finger[16][2] < self.finger[13][2] and self.finger[20][2] < self.finger[17][2]:
                return "down"
        except:
            pass
               
    cv2.waitKey(1)
