import { Component, OnInit } from '@angular/core';
import { items } from './products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})

export class ProductListComponent implements OnInit {
items= items;
  constructor() { }

  ngOnInit(): void {
  }

}
