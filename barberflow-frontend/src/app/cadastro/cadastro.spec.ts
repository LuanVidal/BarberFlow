import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Cadastro } from './cadastro';

describe('Cadastro Component', () => {
  let fixture: ComponentFixture<Cadastro>;
  let component: Cadastro;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Cadastro] 
    }).compileComponents();

    fixture = TestBed.createComponent(Cadastro);
    component = fixture.componentInstance;

    fixture.detectChanges(); 
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });
});
