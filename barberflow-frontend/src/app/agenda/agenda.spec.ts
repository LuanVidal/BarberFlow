import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Agenda } from './agenda';

describe('Agenda Component', () => {
  let fixture: ComponentFixture<Agenda>;
  let component: Agenda;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Agenda] 
    }).compileComponents();

    fixture = TestBed.createComponent(Agenda);
    component = fixture.componentInstance;

    fixture.detectChanges(); o
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });
});
