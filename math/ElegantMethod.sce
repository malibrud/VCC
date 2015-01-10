points = ...
[314 404 0 60;
313 303 0 80 ;
313 230 0 100 ;
313 181 0 120 ;
313 140 0 140 ;
314 106 0 160 ;
314 78  0 180 ;
315 54 0 200  ;
630 403 40 60 ;
543 231 40 100 ;
585 138 60 140 ;
536 76 60 180 ;
115 54 -60 200]

n = size(points, 'r') ;

hFov = 50 * %pi/180.0 ;
vFov = 37 * %pi/180.0 ;
hRes = 635 ;
vRes = 453 ;

Theta = 32 * %pi/180.0 ;

phi = -(Theta + %pi/2) ;

p1z = 64 ;

R = [1 0 0 ;
0 cos(phi)  -sin(phi) ;
0 sin(phi) cos(phi) ] ;

h = 2*tan(vFov/2) ;
w = 2*tan(hFov/2) ;

for i=1:n
    px = points(i,1) ;
    py = points(i,2) ;
    
    x2 = (px - hRes/2)*w/hRes ;
    y2 = (py - vRes/2)*h/vRes ;
    
    v2 = [x2 y2 1]' ;
    v1 = R*v2 ;
    z1 = v1(3) ;
    
    t = -p1z/z1 ;
    
    d = t*v1(1) ;
    e = t*v1(2) ;
    
    u = [d e 0]  ;
    disp(u) ;
    disp(points(i,3:4)) ;

    
end


