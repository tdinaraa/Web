import {Component, OnInit} from '@angular/core';
import {CompanyService} from './company.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  logged = false;

  username = '';
  password = '';

  constructor(private companyService: CompanyService) {}

  ngOnInit(){ //if token exists
    let token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  login() {
    this.companyService.login(this.username, this.password)
      .subscribe(res => {
        console.log(res);

        localStorage.setItem('token', res.token);

      this.logged = true;

        this.username = '';
        this.password = '';
      })
  }

  logout(){
    localStorage.clear();
    this.logged = false;
  }
}
