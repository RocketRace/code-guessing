function spironolactone(R,r,d)
[~,D]=rat(R/abs(r));%D←R÷⍨R∧|r
t=2i*pi*(0:1e-3:D);%t←({○0j2×⍳D×⍵}÷⊢)1000
plot((R-r)*exp(t)+d*exp(t-R/r*t))%]Plot (9∘○{⍺⍵}11∘○) ((R-r)×*t)+d×*t×1-R÷r
end