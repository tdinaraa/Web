import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {items} from './components/shopping-cart/product-list/products';


@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor() { }
  getProduct(id: number): Observable<any> {
    return of(items.find(item => item.id === id));
  }

  getProducts(): Observable<any> {
    return of(items);
  }

  getProductsByCategoryId(id: number): Observable<any> {
    return of(items.filter(item => item.category_id === id));
  }
}
