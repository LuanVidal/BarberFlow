import { TestBed } from '@angular/core/testing';
import { ApiService } from './api.service';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';

describe('ApiService', () => {
  let service: ApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        ApiService,
        provideHttpClient(),        // Habilita o cliente HTTP real
        provideHttpClientTesting()  // Habilita o "Mock" para testes (não bate no Python de verdade)
      ]
    });
    service = TestBed.inject(ApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});