import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompanyService } from '../company.service';
import { Company } from '../company';
import { Vacancy } from '../vacancy';
import { VacancyService } from '../vacancy.service';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {
  vacancies: Vacancy;

  constructor(
    private route: ActivatedRoute,
    private vacancyService: VacancyService,
  ) {}

  ngOnInit(): void {
    this.getVacancyList();
  }

  getVacancyList(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.vacancyService.getVacancyList(id)
      .subscribe(vacancies => this.vacancies = vacancies );
  }




}
