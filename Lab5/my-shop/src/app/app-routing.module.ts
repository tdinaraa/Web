import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {ProductItemComponent} from './components/shopping-cart/product-list/product-item/product-item.component';
import {ProductListComponent} from './components/shopping-cart/product-list/product-list.component';
import {CategoryComponent} from './components/shopping-cart/category/category.component';
import {ProductDetailComponent} from './components/shopping-cart/product-list/product-detail/product-detail.component';

const routes: Routes = [
  {path: 'categories', component:CategoryComponent},
  {path: 'categories/:id/products', component:ProductListComponent},

  // { path: 'products', component: ProductListComponent},

  { path: '', redirectTo: 'categories', pathMatch: 'full'},
  { path: 'products/:id', component: ProductDetailComponent},

  // { path: 'category/:id', component: CategoryComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
