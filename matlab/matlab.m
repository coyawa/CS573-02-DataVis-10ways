x=[];
y=[];
number=[1,1,1,1,1];
for i=1 : size(Manufacturer)    
   if strcmp(Manufacturer(i), 'bmw') 
       x(1, i) = Weight(i);
       y(1, i) = MPG(i);
   elseif strcmp(Manufacturer(i), 'ford')
       x(2, i) = Weight(i);
       y(2, i) = MPG(i);
   elseif strcmp(Manufacturer(i), 'honda')
       x(3, i) = Weight(i);
       y(3, i) = MPG(i);
   elseif strcmp(Manufacturer(i), 'mercedes')
       x(4, i) = Weight(i);
       y(4, i) = MPG(i);
   elseif strcmp(Manufacturer(i), 'toyota')
       x(5, i) = Weight(i);
       y(5, i) = MPG(i);
   end   
end  
spot = Weight/20;
bb = scatter(x(1,:),y(1,:),spot,'y','filled');
hold on
ff=scatter(x(2,:),y(2,:),spot,'m','filled');
hold off
alpha(.5)
hold on
hh=scatter(x(3,:),y(3,:),spot,'c','filled');
hold off
alpha(.5)
hold on
mm=scatter(x(4,:),y(4,:),spot,'r','filled');
hold off
alpha(.5)
hold on
tt=scatter(x(5,:),y(5,:),spot,'g','filled');
hold off
alpha(.5)

axis([1500,5000,0,50])
set(gca,'XTick',1000:1000:5000);
set(gca,'YTick',10:10:50);
xlabel('weight')
ylabel('MPG')

legend([bb ff hh mm tt],'bmw','ford','honda','mercedes','toyota')
