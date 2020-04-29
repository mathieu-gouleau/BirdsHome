import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {HttpHeaders} from '@angular/common/http'
import { Observable } from 'rxjs';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })}

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private httpclient: HttpClient) { }

  private data = [];



  getDatafromBirdHouse():Observable<any>{
    return this.httpclient.get("PUT YOUR IP ADRESS":5000/get",httpOptions)
  }

}
