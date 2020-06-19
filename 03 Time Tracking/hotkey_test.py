from pynput.keyboard import Key, KeyCode, Listener
from sys import exit

class hotkeys:

    # Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)
    # Note the missing `()` after function_1 and function_2 as want to pass the function, not the return value of the function
    
    combination_to_function = {
        frozenset([Key.shift, KeyCode(vk=65)]): function_1,  # shift + a
        frozenset([Key.shift, KeyCode(vk=66)]): function_2,  # shift + b
        frozenset([Key.alt_l, KeyCode(vk=71)]): function_3,  # left alt + g
        frozenset([Key.alt_l, KeyCode(vk=67)]): function_3,  # left alt + c
    }


    # The currently pressed keys (initially empty)
    pressed_vks = set()

    def function_1(self):
        """ One of your functions to be executed by a combination """
        print('Executed function_1')


    def function_2(self):
        """ Another one of your functions to be executed by a combination """
        print('Executed function_2')

    def function_3(self):
        """Quit"""
        print('quitting')
        exit()



    def get_vk(self,key):
        """
        Get the virtual key code from a key.
        These are used so case/shift modifications are ignored.
        """
        return key.vk if hasattr(key, 'vk') else key.value.vk


    def is_combination_pressed(self,combination):
        """ Check if a combination is satisfied using the keys pressed in pressed_vks """
        return all([self.get_vk(self.key) in self.pressed_vks for self.key in combination])


    def on_press(self,key):
        """ When a key is pressed """
        vk = self.get_vk(key)  # Get the key's vk
        print(vk)
        self.pressed_vks.add(vk)  # Add it to the set of currently pressed keys

        for combination in self.combination_to_function:  # Loop through each combination
            if self.is_combination_pressed(combination):  # Check if all keys in the combination are pressed
                self.combination_to_function[combination]()  # If so, execute the function


    def on_release(self,key):
        """ When a key is released """
        vk = self.get_vk(key)  # Get the key's vk
        self.pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys

    def start_listener(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()



print ('class testing')
hot = hotkeys()
hot.start_listener()