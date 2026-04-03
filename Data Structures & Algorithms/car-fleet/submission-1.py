class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        steps = []
        for i, pos in enumerate(position):
            step = (target - pos)/speed[i]
            steps.append(step)
        
        s_pos, s_steps = map(list,zip(*sorted(zip(position, steps), reverse=True)))
        fleet = 1
        print(s_pos, s_steps)
        for i in range(len(s_steps)-1):
            turn = s_steps[i]
            n_turn = s_steps[i+1]
            if (n_turn <= turn):
                s_steps[i+1] = turn
            else:
                fleet += 1
        return fleet
            


                

        
        # return fleet 
                
            
        


        [4, 1, 0 , 7, 8, 3]
        # [2, 2, 1, 1, 1, 1]
        [3, 5, 10, 3, 2, 7]
