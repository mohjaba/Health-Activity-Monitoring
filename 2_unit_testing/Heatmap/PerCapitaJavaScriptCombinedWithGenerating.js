
var map;
var heatmap;
var heatmapData=[];




var NYwgt=1, LAwgt=1, CHGOwgt=1, HSTwgt=1, JAXwgt=1, DNVwgt=1, SEAwgt=1;


var NYdata= new Array(NYwgt,40.6643,-73.9385,8504);
var LAdata= new Array(LAwgt,34.0194,-118.4108,3884);
var CHGOdata= new Array(CHGOwgt,41.8376,-87.6818,2718);
var HSTdata= new Array(HSTwgt,29.7805,-95.3863,2195);
var JAXdata= new Array(JAXwgt,30.3370,-81.6613,842);
var DNVdata= new Array(DNVwgt,47.6205,-122.3509,649);
var SEAdata= new Array(SEAwgt,39.7618,-104.8806,652);


var cityData= new Array(NYdata,LAdata,CHGOdata,HSTdata,JAXdata,DNVdata,SEAdata);


var sumOfPop=0;
for (i=0;i<7;i++)
{
	sumOfPop=sumOfPop + cityData[i][3];
}

EqualProb = new Array(1/7,1/7,1/7,1/7,1/7,1/7,1/7);
PopBasedProb = new Array(7)
for (i=0;i<PopBasedProb.length;i++)
{
	PopBasedProb[i]=cityData[i][3]/sumOfPop;
}
MixedProb = new Array(7)
for (i=0;i<7;i++)
{
	MixedProb[i]=(EqualProb[i]+PopBasedProb[i])/2;
}

function DeclareData(prob)
{

var NYdata= new Array(NYwgt,40.6643,-73.9385,8504);
var LAdata= new Array(LAwgt,34.0194,-118.4108,3884);
var CHGOdata= new Array(CHGOwgt,41.8376,-87.6818,2718);
var HSTdata= new Array(HSTwgt,29.7805,-95.3863,2195);
var JAXdata= new Array(JAXwgt,30.3370,-81.6613,842);
var DNVdata= new Array(DNVwgt,47.6205,-122.3509,649);
var SEAdata= new Array(SEAwgt,39.7618,-104.8806,652);


var cityData= new Array(NYdata,LAdata,CHGOdata,HSTdata,JAXdata,DNVdata,SEAdata);


var RandChoseCities = new Array(7);

function generateRandomData(Cities,probability,numOfDataPoints)
{
	for (i=0;i<7;i++)
	{
		Cities[i]=0;
	}


	for (k=0;k<numOfDataPoints;k++)
	{
		var sumOfProb=0;
		var rndNum=Math.random();
		for(j=0;j<7;j++)
		{
			if(rndNum>sumOfProb && rndNum <= sumOfProb+probability[j])
			{Cities[j]=Cities[j]+1;}
			sumOfProb=sumOfProb+probability[j];
		}

	}

}



RunningMapData = [
  {location: new google.maps.LatLng(40.6643 ,-73.9385), weight: NYwgt},
  
];

generateRandomData(RandChoseCities,prob,400);





num=0;
for(q=0;q<7;q++)
{
	for(l=0;l<RandChoseCities[q];l++)
	{
		var latLng = new google.maps.LatLng(cityData[q][1], cityData[q][2]);
		var weightedLoc = 
		{
      		location: latLng,
      		weight: cityData[q][0]
   		};
		RunningMapData.push(weightedLoc);
		
	}
}
}


//*************************************************************************



	DeclareData(EqualProb);
	

      function initialize() {
  
        var mapOptions = {
          center: new google.maps.LatLng(39.833333, -98.583333),
          zoom: 4,
          mapTypeId: google.maps.MapTypeId.SATELLITE

        }

	var mapCanvas = document.getElementById('map_canvas');

        map = new google.maps.Map(mapCanvas, mapOptions)
      


	heatmap = new google.maps.visualization.HeatmapLayer({
	data: RunningMapData,
		radius:75

	});


	heatmap.setMap(map);

	}

google.maps.event.addDomListener(window, 'load', initialize);

function ChooseRegHeatMapEqualProb()
{
	NYwgt=1, LAwgt=1, CHGOwgt=1, HSTwgt=1, JAXwgt=1, DNVwgt=1, SEAwgt=1;
	DeclareData(EqualProb);
	initialize();
}


function ChooseRegHeatMapPopBasedProb()
{
	NYwgt=1, LAwgt=1, CHGOwgt=1, HSTwgt=1, JAXwgt=1, DNVwgt=1, SEAwgt=1;
	DeclareData(PopBasedProb);
	initialize();
}


function ChooseRegHeatMapMixedProb()
{
	NYwgt=1, LAwgt=1, CHGOwgt=1, HSTwgt=1, JAXwgt=1, DNVwgt=1, SEAwgt=1;
	DeclareData(MixedProb);
	initialize();
}




function ChoosePerCapitaHeatMapEqualProb()
{
	NYwgt=1, LAwgt=(8405.0/3884.0), CHGOwgt=(8405.0/2718.0), HSTwgt=(8405.0/2195.0), JAXwgt=(8405.0/842.0), DNVwgt=(8405.0/649.0), SEAwgt=(8405.0/652.0);

	DeclareData(EqualProb);
	initialize();
}

function ChoosePerCapitaHeatMapPopBasedProb()
{
	NYwgt=1, LAwgt=(8405.0/3884.0), CHGOwgt=(8405.0/2718.0), HSTwgt=(8405.0/2195.0), JAXwgt=(8405.0/842.0), DNVwgt=(8405.0/649.0), SEAwgt=(8405.0/652.0);

	DeclareData(PopBasedProb);
	initialize();
}

function ChoosePerCapitaHeatMapMixedProb()
{
	NYwgt=1, LAwgt=(8405.0/3884.0), CHGOwgt=(8405.0/2718.0), HSTwgt=(8405.0/2195.0), JAXwgt=(8405.0/842.0), DNVwgt=(8405.0/649.0), SEAwgt=(8405.0/652.0);

	DeclareData(MixedProb);
	initialize();
}	
