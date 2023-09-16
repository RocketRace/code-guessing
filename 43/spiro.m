function spironolactone(R,r,d)
[~,D]=rat(R/abs(r));
t=2i*pi*(0:1e-3:D);
plot((R-r)*exp(t)+d*exp(t-R/r*t))
end