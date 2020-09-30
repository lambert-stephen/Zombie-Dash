# class Button:
#     def __init__(self, image, position, callback):
#         self.image = image
#         self.rect = image.get_rect(topleft=position)
#         self.callback = callback
#     def on_click(self, event):
#         if event.button == 1:
#             if self.rect.collidepoint(event.pos):
#                 self.callback(self)

class Button:
    def __init__(self, image, position, callback):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.callback = callback

    def on_click(self, event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
               if self.callback :
                   self.callback=False;
               else :
                   self.callback=True;