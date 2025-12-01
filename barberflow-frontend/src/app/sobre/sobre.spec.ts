import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Sobre } from './sobre';

describe('Sobre Component', () => {
  let fixture: ComponentFixture<Sobre>;
  let component: Sobre;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Sobre]
    }).compileComponents();

    fixture = TestBed.createComponent(Sobre);
    component = fixture.componentInstance;
    fixture.detectChanges(); 
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });
});
