from django.shortcuts import render  
from vehicle_forms.forms import VehicleForm  
  
def add(response):  
    # Here we just create an object for the StudentForm Class and fetch data and send to output.html
    if response.method == 'POST':
        vehicle = VehicleForm(response.POST)
        if vehicle.is_valid():
            a=[]
            b=[]
            c=[]
            sum=0
            sum1=0
            shipment=vehicle.cleaned_data['shipments']
            for i in range(shipment):
                wt=vehicle.cleaned_data['weights']
                weight = list(map(int, wt.strip().split()))[:shipment]

            weight.sort()
            
            for i in range(0,shipment):
                
            
                if weight[i]<50 and sum<=250:
                    
                    b.append(weight[i])
                elif weight[i]>=50:
                    sum1=sum1+weight[i]
                    if sum1<=250:
                        a.append(weight[i])
                    else:
                        c.append(weight[i])
                        return render(response, 'output.html', {'message1': a ,'message2':  b,'message3':  c})
        else:
            return render(response, 'details.html', {'form': vehicle})
    else:
        vehicle = VehicleForm() 
        return render(response, 'details.html', {'form': vehicle})