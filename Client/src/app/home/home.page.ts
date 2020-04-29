import { Component, ChangeDetectorRef } from '@angular/core';
import { DataService } from '../service/data.service';
import { Subscription } from 'rxjs';


@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  constructor(private cd: ChangeDetectorRef, private _ApiCallService:DataService) {}

  sub: Subscription;
  birdsInHouse:boolean;
  data: number;
  // lstBirdsdata = [{passages:];
  lstBirdsdata = [{passages:0}]
  ngOnInit(): void {
    
  }

  ngOnDestroy() {
    if (this.sub != null) {
        this.sub.unsubscribe();

    }
  }

  DisplayData(){
    this.sub = this._ApiCallService.getDatafromBirdHouse().subscribe((data)=>{
      if (data !==null){
        this.lstBirdsdata = [];
        this.lstBirdsdata.push({passages: data})
        console.log("el primero "+this.lstBirdsdata[0].passages)
        console.log(this.lstBirdsdata[0].passages)
        if (this.lstBirdsdata[0].passages>100){
          this.birdsInHouse = true;
        }
        else{
          this.birdsInHouse = false;
        }
        this.cd.detectChanges();
      }
    });
    
  }
  

}
