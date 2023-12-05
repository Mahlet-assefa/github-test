class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        total=sum(distance)
        if start < destination:
            route1=sum(distance[start: destination])
        else:
            route1=sum(distance[destination: start])
        route2=total-route1
        
        return min(route1,route2)    
        
            
