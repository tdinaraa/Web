import { Component, OnInit, Input } from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {ProductService} from  '../.../../../../../product.service';
import {CategoryService} from  '../.../../../../../category.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {
item: any;
  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private productService: ProductService,
    private categoryService: CategoryService
  ) {
    this.router.events.subscribe((value =>{
      this.getProduct();
    }));
  }

  ngOnInit(): void {
    this.getProduct();
  }
  getProduct() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id).subscribe(item => this.item = item);
  }
}
