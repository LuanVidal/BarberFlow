import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Sobre } from './sobre';

describe('Sobre', () => {
  let component: Sobre;
  let fixture: ComponentFixture<Sobre>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Sobre]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Sobre);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
